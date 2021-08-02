# -*- coding: utf-8 -*-
# author：xuanlong
# 创建：2021-07-18
# 更新：2012-07-18
# 用意：基本函数模块getCutWords、JudgeArticle、getclass、sentimentFunc ，组合模块：重写评论
# MacOS 无法读取文件时，注意删除.DS_Store文件


import jieba
import json
import os
import jieba.posseg as pseg

from gloPath import globalPath,writePath
from basicProcess import getArticle,stopwordslist


from snownlp import SnowNLP

def cal(conts):
    num = 0
    senti = 0
    for content in conts:
        proWords = getCutWords(content)
        score = sentimentFunc(proWords)
        print(num,proWords,score)
        try:
            senti  = senti + score
            num = num + 1
        except:
            print('senti value error')
    try:    
        finalsenti = senti/num
        return finalsenti
    except:
        print('ZeroDivisionError')

# 返回切完词的文件的内容
def getCutWords(d):  
    '''
    返回切完词的文件，对词性进行标注
    :d :切词内容
    :return : 切完词后的内容
    '''
    cutWords = ''
    c = []
    # 进行切词
    seg_list = pseg.cut(d)
    #cutWords = ["'".join(seg_list)]
    stopwords = stopwordslist()
    
    for w in seg_list:
        if w not in stopwords:
            try:
                if w.flag == 'n' or w.flag == 'v' or w.flag == 'y':
                    cutWords = cutWords + w.word
                    # c.append(w.word)
                else:
                    pass
                    # print("cutwords error")
            except:
                print('words flag error')
    return cutWords
    # return cutWords

# 获取12-5月的全部文章内容，并写入路径allArticles.txt
def getAllArticles(fileName):
    '''
    所有内容整合至一个文件
    :fileName: 文件内容
    : return 直接写入
    '''
    # writeAllArticlesPath = writePath().allArticles()    
    with open(fileName, 'r', encoding= 'utf-8') as fr:
        data = json.load(fr)
        c = getArticle(data)
        # 一篇文章写一行，全部写入一个文件
        # @getAllArticles
        # open(writeAllArticlesPath,'a+',encoding= 'utf-8') as fw:
        #     fw.write(c + '\n')

def addinfo(path,num,FindName):
    '''
    增加分类
    :path : 源文件
    :num : 文章序号
    :FindName :重写后的文件
    '''
    with open(path,'r',encoding='utf-8') as fr:
        data = json.load(fr)
        for i in data:
            print(i)
            addition = {}
            addition['number'] = num
            addition['class'] = getclass(i)
            i['property'] = addition
            
            try:
                jsonStr = json.dumps(i,indent=4,ensure_ascii=False)
                with open(FindName,'a+',encoding= 'utf-8') as fw:
                    fw.write(jsonStr + ',' + '\n')
            except:
                print('content error')
            
            num = num + 1
        return num

def dict2json(the_dict):
    '''
    将字典文件写如到json文件中
    :param file_name: 要写入的json文件名(需要有.json后缀),str类型
    :param the_dict: 要写入的数据，dict类型
    :return: 1代表写入成功,0代表写入失败
    '''
    file_name = r'test1.txt'
    try:
        json_str = json.dumps(the_dict,indent=4,ensure_ascii=False)
        with open(file_name, 'a+') as json_file:
            json_file.write(json_str+',' +'\n')
        return 1
    except:
        return 0   

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
        print('snowNlp can not excuate!')
        
# 没有一样的值返回True,有返回False
def JudgeArticles(k,keywords):
    '''
    判别分词内容是否在主题词表
    :k 分词后内容
    :keywords: 聚类后写入的主题词表
    :return :有一样的值返回True，没有一样的的返回False
    '''
    v = set(k).isdisjoint(set(keywords))
    return v
      
def getclass(i):
    '''
    获取文章分类
    :i : 文章内容
    :return :分类
    '''
    with open('Data/processFile/paper/writeFolder/topicWords/econmicTopic.txt') as f:
        content = f.readlines()
        econmicTopic = [x.strip() for x in content]
        # print(econmicTopic)
    with open('Data/processFile/paper/writeFolder/topicWords/epicTopic.txt') as f:
        content = f.readlines()
        epicTopic = [x.strip() for x in content]
        # print(epicTopic)
    with open('Data/processFile/paper/writeFolder/topicWords/politicTopic.txt') as f:
        content = f.readlines()
        politicTopic = [x.strip() for x in content]
        # print(politicTopic)
        
    # 关键词 old methods
    # k = i['meta']['keyword']
    # k1 = k.split(',')

    # 分词 按照词频筛选
    c = i['meta']['content']
    k2 = getCutWords(c)
    
    z = k2 
    # print(k)
    
    vEconmic = JudgeArticles(z,econmicTopic)
    vEpicTopic = JudgeArticles(z,epicTopic)
    vPoliticTopic = JudgeArticles(z,politicTopic)
    
    v = [] 
    if vEconmic is False:
        v.append('经济')
    elif vEpicTopic is False:
        v.append('疫情')
    elif vPoliticTopic is False:
        v.append('政治')
    elif vEconmic and vEpicTopic and vPoliticTopic:
        v.append('其他')
    else:
        pass
       
    return v

if __name__ =="__main__":
    # num = 0 
    # commentPath = globalPath().dataSet('comment')
    # metaDataPath = globalPath().dataSet('data') 
    
    # AllArticlesPath = writePath().allArticles('original')
    # AllArticlesPathFenci = writePath().allArticles('fenci')
    # FinalcommentPath = globalPath().FinaldataSet('comment')
    # FinalmetaDataPath = globalPath().FinaldataSet('data') 
    
    metaDataPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/newdata'
    FinalmetaDataPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/newFinaldata'
    
    # 全部新闻文章分词
    files= os.listdir(metaDataPath)
    files.sort()
    for file in files:
        print(file)
        fileName = metaDataPath + '/' + file
        FindName = FinalmetaDataPath +'/' + file
        print(fileName)
        print(FindName)

        with open(fileName,'r',encoding='utf-8') as fr:
            data = json.load(fr)
            for i in data:
                content = i['meta']['content']
                conts = content.split('。')[:-1]
                s = cal(conts)
                i['sentiment'] = s
                
                try:
                    jsonStr = json.dumps(i,indent=4,ensure_ascii=False)
                    with open(FindName,'a+',encoding= 'utf-8') as fw:
                        fw.write(jsonStr + ',' + '\n')
                except:
                    print('content error')
                
                # print(c)
'''
                addition = {}
                addition['number'] = num
                addition['class'] = getclass(i)
                
                i['property'] = addition
                i['sentiment'] = sentimentFunc(c)
'''
                
                
                # num = num + 1

        
    # @ all articles cut words
    # with open(AllArticlesPath, 'r' , encoding= 'utf-8') as fr:
    #     for line in fr:
    #         print('----running----')
    #         c = getCutWords(line)
    #         with open(AllArticlesPathFenci,'a+', encoding= 'utf-8') as fr:
    #             fr.write(c)
    #             fr.close()
        

    
    # for file in files:
    #     print(file)
    #     fileName = metaDataPath + '/' + file
    #     getAllArticles(fileName)
        
            
    
    
    
    
    
    
    
    
    
    