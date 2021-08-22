# -*- coding: utf-8 -*-
# author：xuanlong
# 创建：2021-07-18
# 更新：2012-07-18
# 用意：疫情文章的总情感趋势、疫情评论的总情感趋势
# MacOS 无法读取文件时，注意删除.DS_Store文件

import os 
import json
from snownlp import SnowNLP
        
# 返回该日的疫情相关的文章的评论数量和评论分数
def getComment(data,urls):
    countComments = 0
    scoreComments = 0
    for line in data:
        d = line['comment']
        u = line['url']
        # 找出对应文章
        if u in urls:
            if len(d):
                for comment in d:
                    countComments = countComments + 1
                    s = comment['sentiment']
                    try:
                        if str(s) == 'null':
                            continue
                        else:
                            scoreComments = scoreComments + s
                    except:
                        print('comment sentiment is error')
            else:
                continue
                # countComments = countComments + 0
                # scoreComments = scoreComments + 0
    return countComments,scoreComments
    


# 没有一样的值返回True,有返回False
def JudgeArticles(k,keywords):
    v = set(k).isdisjoint(set(keywords))
    return v

# 返回该日的疫情文章数量、文章分数,Url
def getContent(data):
    countArticles = 0
    socreArticles = 0
    urls = []
    for line in data:
        #print(line)
        url = line['url']
        # 没有一样的值返回True,有返回False
        # v = JudgeArticles(k,keywords)
        classId = line['property']['class']
        s = line['sentiment']
        #print(s)
        if '疫情' in classId:
            #表明为该分类的相关文章
            countArticles = countArticles + 1
            try:
                if str(s) == 'null':
                    print('sentiment is null')
                    continue
                else:
                    socreArticles = socreArticles + s
            except:
                print('articles sentiment error')
            urls.append(url)
        else:
            continue
            # countArticles = countArticles + 0
            # socreArticles = socreArticles + 0
            
            # print(countArticles)
    return countArticles,socreArticles,urls



if __name__ =="__main__":
    # 写入文本"疫情文章的总情感趋势,疫情评论的总情感趋势"
    writeFile = 'Final_comments_epidemic_v5.txt'   
    
    # 文章
    SinaNewsMetaPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/reSingleData'
    print(SinaNewsMetaPath)
    # 评论
    SinaNewsCommentPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/newcomment'
    
    files= os.listdir(SinaNewsMetaPath)
    files.sort()
    
    # 对每个文件操作
    for file in files:
        print(file)
        # 输出路径
        str1 = '2020-' + file   
        str2 = str1.split('.')[0]

        # FindedName 里面只有文章的内容
        FindedName = SinaNewsMetaPath + '/' + file
        # CommentName 里面有评论
        CommentName = SinaNewsCommentPath + '/' + file

        print(FindedName)
        print(CommentName)
        
        # 返回该日的文章数量、文章分数
        with open(FindedName,'r',encoding= 'utf-8') as fileOpen:
            try:
                data = json.load(fileOpen)
                countArticles, socreArticles, urls = getContent(data)
                # print(countArticles,socreArticles)
                avgA = socreArticles/countArticles
            except:
                print('articles input error')

        # 返回该日的评论数量、评论分数
        with open(CommentName,'r', encoding= 'utf-8') as fileOpenT:
            try:
                dataT = json.load(fileOpenT)
                countComments,scoreComments = getComment(dataT,urls)
                avgC = scoreComments/countComments
            except:
                print('comments input error')
            
        with open(writeFile,'a+',encoding='utf-8') as w:
            # 日期，文章数，文章分数，评论数，评论分数, 文章情感均值，评论情感均值
            w.write(str2 + ',' + str(countArticles) + ',' + str(socreArticles) + ',' 
            + str(countComments) + ',' +str(scoreComments) +','
            + str(avgA) + ',' + str(avgC) + '\n')
        



