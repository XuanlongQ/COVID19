
# -*- coding: utf-8 -*-

import json
import os

wuhanList = ['湖北武汉','武汉']

def findAddition(u,fileName):
    with open(fileName,'r', encoding= 'utf-8') as fr:
        data = json.load(fr)
        for line in data:
            url = line['url']
            p = line['property']
            if u == url:
                return p
            else:
                continue

def rewriteWuhanComments(data,fileName,outputName):
    for line in data:
        d = line['comment']
        u = line['url']
        if len(d):
            p = findAddition(u,fileName)
            line['property'] = p
            
            jsonStr = json.dumps(line,indent=4,ensure_ascii=False)
            with open(outputName,'a+',encoding= 'utf-8') as fw:
                fw.write(jsonStr + ',' + '\n')
            
        else:
            continue
    return 0
        
    
def getComment(data):
    countArticles = 0
    countComments = 0
    scoreComments = 0
    for line in data:
        d = line['comment']
        # 找出对应文章
        u = line['url']
        classId = line['property']['class']
        if '经济' in classId:
            countArticles = countArticles + 1
            if len(d):
                # 返回这篇文章的分类
                # findClass(u,file)
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
        else:
            continue
            
        # 评论不为空
        
    return countArticles,countComments,scoreComments

if __name__ == '__main__':
   #  writeFile = r'wuhanComments_v2.txt'
    
    # SinaNewsMetaPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/data'
    # print(SinaNewsMetaPath)
    
    wuhanComment = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/wuhanFinalComment'
    outputPath = r'wuhanDataEconmic.txt'
    files= os.listdir(wuhanComment)
    files.sort()
    
    for file in files:
        # fileName = SinaNewsMetaPath + '/' + file
        FindName = wuhanComment + '/' + file
        # outputName = outputPath + '/' + file
        
        str1 = '2020-' + file   
        str2 = str1.split('.')[0]
        
        
        with open(FindName,'r',encoding='utf-8') as fr:
            data = json.load(fr)
            countArticles,countComments,scoreComments = getComment(data)
            try:
                avg = scoreComments/countComments
            except Exception as e:
                print(e)
                
            with open(outputPath,'a+',encoding= 'utf-8') as fw:
                fw.write(str2 + ',' + str(countArticles) + ',' + str(countComments) + ',' + str(scoreComments) + ',' + str(avg) + '\n' )
            # newline = rewriteWuhanComments(data,fileName,outputName)
            
            
        

 

            
  
                
            
'''
            for line in data:
                wuhandata = {}
                addition = []
                
                c = line['comment']
                if len(c):
                    # print(c)
                    for comment in c:
                        area = comment['area']
                        if area in wuhanList:
                            
                            newDict = {}
                            newDict['area'] = comment['area']
                            newDict['content'] = comment['content']
                            newDict['nickname'] = comment['nickname']
                            newDict['reply_to'] = comment['reply_to']
                            newDict['sentiment'] = comment['sentiment']
                            
                            addition.append(newDict)
                            
                        else:
                            continue
                    wuhandata['comment'] = addition
                    wuhandata['time'] = line['time']
                    wuhandata['title'] = line['title']
                    wuhandata['url'] = line['url']
                    
                    try:
                        jsonStr = json.dumps(wuhandata,indent=4,ensure_ascii=False)
                        with open(FindName,'a+',encoding= 'utf-8') as fw:
                            fw.write(jsonStr + ',' + '\n')
                    except:
                        print('content error')
                else:
                    continue

'''

