
# -*- coding: utf-8 -*-

import json
import os

#wuhanList = ['湖北武汉','武汉']

wuhanPath = r'epidemicComment.txt'

def allwuhanComments(FindName):
    global wuhanPath
    with open(FindName,'r',encoding= 'utf-8') as fr:
        data = json.load(fr)
        for line in data:
            d = line['comment']
            u = line['url']
            timeT = line['time']
            t = timeT.split(' ')[0]
            classId = line['property']['class']
            if '疫情' in classId:
                if len(d):
                    for comment in d:
                        s = comment['sentiment']
                        content = comment['content']
                        cfinal = content.replace('\n', '').replace('\r', '')
                        with open(wuhanPath,'a+',encoding='utf-8') as fw:
                            fw.write(str(t) + ',' + str(u) + ',' + str(classId) + ',' + str(s) + ',' + str(cfinal) + '\n')
                            fw.close()
                else:
                    continue       
            else:
                continue
            
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

def getArticles(data):
    countArticles = 0
    scoreArticles = 0
    positive = 0
    negative = 0
    netural = 0
    for line in data:
        classId = line['property']['class']
        if '政治' in classId:
            countArticles += 1
            s = line['sentiment'] 
            if str(s) == 'null' or str(type(s)) == "<class 'NoneType'>":
                continue
            else:
                scoreArticles = scoreArticles + s
                if s <= 0.3:
                    negative += 1
                elif s > 0.7:
                    positive += 1
                else:
                    netural += 1   
        else:
            continue
    return countArticles,scoreArticles,positive,netural,negative
           
def getComment(data):
    countArticles = 0
    countComments = 0
    scoreComments = 0
    positive = 0
    negative = 0
    netural = 0
    
    for line in data:
        d = line['comment']
        # 找出对应文章
        u = line['url']
        classId = line['property']['class']
        if '疫情' in classId:
            countArticles = countArticles + 1
            if len(d):
                # 返回这篇文章的分类
                # findClass(u,file)
                for comment in d:
                    countComments = countComments + 1
                    s = comment['sentiment']
                    if s <= 0.3:
                        negative += 1
                    elif s > 0.7:
                        positive += 1
                    else:
                        netural += 1
                        
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
        
    return countArticles,countComments,scoreComments,positive,netural,negative

if __name__ == '__main__':
   #  writeFile = r'wuhanComments_v2.txt'
    
    # 所有内容统计
    # SinaNewsMetaPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/data'
    # print(SinaNewsMetaPath)
    
    #wuhanComment = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/wuhanFinalComment'
    
   
    # metaData = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/data'
    # outputPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/allCommentwithClass'
    
    # 除了武汉区域的情感数和均值
    # otherComment = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/newcomment'
    
    # 所有评论增加分类
    newComment = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/internationalData/comments'
    outputPath = r'allCommentEpidemic_intl.txt'
    
    files= os.listdir(newComment)
    files.sort()
    
    for file in files:
        FindName = newComment + '/' + file
        # fileName = SinaNewsMetaPath + '/' + file
        # outputName = outputPath + '/' + file
        
        str1 = '2020-' + file   
        str2 = str1.split('.')[0]
        
        with open(FindName,'r',encoding='utf-8') as fr:
            data = json.load(fr)
            countArticles,countComments,scoreComments,positive,netural,negative = getComment(data)
            try:
                avg = scoreComments/countComments
                with open(outputPath,'a+',encoding= 'utf-8') as fw:
                    fw.write(str2 + ',' + str(countArticles) + ',' + str(countComments) + ',' + str(scoreComments) + ',' + str(avg) +','
                            + str(positive) + ',' + str(netural)+ ',' + str(negative) + '\n' )
            except Exception as e:
                print(e)
                
            
            
            # for line in data:
                
                
            #     wuhandata = {}
            #     addition = []
            #     # print(line)
                
            #     c = line['comment']
            #     u = line['url']
            #     if len(c):
            #         # print(c)
            #         for comment in c:
            #             # area = comment['area']
            #             # if area not in wuhanList:  
            #             newDict = {}
            #             newDict['area'] = comment['area']
            #             newDict['content'] = comment['content']
            #             newDict['nickname'] = comment['nickname']
            #             newDict['reply_to'] = comment['reply_to']
            #             newDict['sentiment'] = comment['sentiment']
                        
            #             addition.append(newDict)
                            
            #             # else:
            #             #     continue
            #         wuhandata['comment'] = addition
            #         wuhandata['time'] = line['time']
            #         wuhandata['title'] = line['title']
            #         wuhandata['url'] = line['url']
            #         pro = findAddition(u,fileName)
            #         wuhandata['property'] = pro
            #         #print(wuhandata)
                    
            #         try:
            #             jsonStr = json.dumps(wuhandata,indent=4,ensure_ascii=False)
            #             with open(outputName,'a+',encoding= 'utf-8') as fw:
            #                 fw.write(jsonStr + ',' + '\n')
            #         except:
            #             print('content error')
            #     else:
            #         continue
        
        
        
        # with open(FindName,'r',encoding='utf-8') as fr:
        #     data = json.load(fr)
        #     countArticles,countComments,scoreComments,positive,netural,negative= getComment(data)
        #     try:
        #         avg = scoreComments/countComments
        #     except Exception as e:
        #         print(e)
                
        #     with open(outputPath,'a+',encoding= 'utf-8') as fw:
        #         fw.write(str2 + ',' + str(countArticles) + ',' + str(countComments) + ',' + str(scoreComments) + ',' + str(avg) +','
                        #  + str(positive) + ',' + str(netural)+ ',' + str(negative) + '\n' )
            # newline = rewriteWuhanComments(data,fileName,outputName)
             
        
        #allwuhanComments(FindName)    

        # 找出武汉/非武汉的评论


  
