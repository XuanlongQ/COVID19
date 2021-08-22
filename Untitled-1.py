# -*- coding: utf-8 -*-
import json
import os
# from snownlp import SnowNLP

# s1 = r'厉害👍'
# s = SnowNLP(s1)
# score = s.sentiments
# print(score)

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

if __name__ == '__main__':
    SinaNewsMetaPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/internationalData/articles'
    outputPath = r'allarticlesPolitic_intl.txt'
    
    files= os.listdir(SinaNewsMetaPath)
    files.sort()
    
    
    
    for file in files:
        
        str1 = '2020-' + file   
        str2 = str1.split('.')[0]
        
        fileName = SinaNewsMetaPath + '/' + file
        with open(fileName,'r',encoding='utf-8') as fr:
            data = json.load(fr)
            countArticles,scoreArticles,positive,netural,negative = getArticles(data)
            try:
                avg = scoreArticles/countArticles
                with open(outputPath,'a+',encoding= 'utf-8') as fw:
                    fw.write(str2 + ',' + str(countArticles) + ',' + str(scoreArticles) +  ',' + str(avg) +','
                            + str(positive) + ',' + str(netural)+ ',' + str(negative) + '\n' )
                    fw.close()
            except Exception as e:
                print(e)
                
            
            
