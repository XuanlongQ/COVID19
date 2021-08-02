# -*- coding: utf-8 -*-
# 采样统计函数
import json
import random
import os

def sampleContent(n):
    path = r'/Users/xuanlongqin/Documents/data/covid-19/Data/processFile/paper/dataSet/Finaldata2/01-03.txt'
    with open(path,'r',encoding= 'utf-8') as fr:
        data = json.load(fr)
        for line in data:
            number = line['property']['number']
            if number == n:
                return n, line
            else:
                continue
    

if __name__ == '__main__':

    rpath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/wuhanCommentClass'
    wpath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/wuhanFinalCommen'
    files= os.listdir(rpath)
    files.sort()
    for file in files:
        print(file)
        fileName = rpath + '/' + file
        FindName = wpath +'/' + file
        with open(fileName,'r',encoding='utf-8') as f:
            content = f.read()
            a = content.strip('\n').strip(',')
            with open(FindName,'w',encoding= 'utf-8') as fw:
                fw.write('[' + a + ']')
    
    
    # x = random.randint(0,50)
    # n,content = sampleContent(x)
    # print(n)
    # print(content)

    
    
    
    
    
    