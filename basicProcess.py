# -*- coding: utf-8 -*-
# author：xuanlong
# 创建：2021-07-18
# 更新：2012-07-1
# 用意：基本函数模块getComment、getArticle、stopwordslist、sentimentFunc ，组合模块：重写评论
# MacOS 无法读取文件时，注意删除.DS_Store文件

import json
import os 
import pandas as pd 
from snownlp import SnowNLP

from gloPath import globalPath,writePath


def txtToCsv(path):
    '''
    txt 写入CSV
    :param : 文件
    // 评论为0的值需要进行了手工剔除
    // 文章数小于10 ，情感值为1 ，需要手工剔除
    
    '''
    df = pd.read_csv(path,header=None,names = ['日期','文章数','文章分数','评论数','评论分数','文章情感均值','评论情感均值'])
    df.to_csv('Final_comments_epidemic_v3.csv',encoding = 'utf_8_sig')



def getComment(data):
    '''
    全局模块，获取该日的评论内容，存在改写 
    :data : 每日的评论
    :return : 当前函数返回评论内容，如需8返回其他内容请改写
    '''
    count = 0
    for line in data:
        count = count + 1
        c = line['comment']
        t = line['time']
        title = line['title']
        u = line['url']
        for comment in c:
            area = comment['area']
            content = comment['content']
        return c,count


def getArticle(data):
    '''
    全局模块，获取改日的文章内容，存在改写 //改写模块已注释
    :data : 每日的文章
    :return : 当前函数返回文章内容，如需返回其他内容请改写
    '''
    for line in data:
        c = line['meta']['content']
        d = line['meta']['description']
        k = line['meta']['keyword']
        url = line['url']
        # 一篇文章写一行，全部写入一个文件
        # with open(writeAllArticlesPath,'a+',encoding= 'utf-8') as fw:
        #     fw.write(c + '\n')
        return c
        

def stopwordslist():
    '''
    停用词设置
    :stopword :百度停用词表，哈工大停用词表，中文停用词表，四川大学机器智能实验室停用词库 //统一整合至cn_stopwords
    
    '''
    stopwords = [line.strip() for line in open('/Users/xuanlongqin/Documents/data/covid-19/Data/processFile/COVID19Analyis/writeFolder/stopWords/cn_stopwords.txt',encoding='UTF-8').readlines()]
    return stopwords

def sentimentFunc(c):
    '''
    情感分析模块，获取情感分析值
    :param c: 评论内容
    :return : 情感分析值
    '''
    try:
        s = SnowNLP(c)
        score = s.sentiments
        return score
    except:
        return None
        print('snowNlp can not excuate!')

def reWrite(path,FindName):
    '''
    获取评论的情感分析值，重写json文件
    :param path: 原始评论地址
    :param FindName: 写入地址
    :param return : 无 直接写入
    '''
    with open(path,'r',encoding='utf-8') as fr:
        data = json.load(fr)
        for line in data:
            jdata = {}
            
            c = line['comment']
            addition = []
            for comment in c:
                newDict = {}
                #print(comment)
                s = comment['area']
                newDict['area'] = comment['area']
                newDict['content'] = comment['content']
                newDict['nickname'] = comment['nickname']
                newDict['reply_to'] = comment['reply_to']
                # newDict['time'] = comment['time']
                newDict['sentiment'] = sentimentFunc(s)
                addition.append(newDict)
            # print(addition)
                
            jdata['comment'] = addition
            jdata['time'] = line['time']
            jdata['title'] = line['title']
            jdata['url'] = line['url']
            
            try:
                jsonStr = json.dumps(jdata,indent=4,ensure_ascii=False)
                with open(FindName,'a+',encoding= 'utf-8') as fw:
                    fw.write(jsonStr + ',' + '\n')
            except:
                print('content error') 
        
        
if __name__ =="__main__":
    commentPath = globalPath().dataSet('comment')
    # commentPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/processFile/paper/dataSet/sinaNews/comment'
    FinalcommentPath = globalPath().FinaldataSet('comment')
    # FinalcommentPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/processFile/paper/dataSet/sinaNews/finalcomment'
    
    

    print(commentPath)
    files= os.listdir(commentPath)
    files.sort()
    for file in files:
        fileName = commentPath + '/' + file
        FindName = FinalcommentPath +'/' + file
        print(fileName)
        reWrite(fileName,FindName)

        