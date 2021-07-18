# -*- coding: utf-8 -*-
# author：xuanlong
# 创建：2021-07-18
# 更新：2012-07-18
# 用意：dataset 为最初数据，未加addition 字段 ，FinaldataSet 加入了 additioanal 字段，需要组合路径
# MacOS 无法读取文件时，注意删除.DS_Store文件

class globalPath:
    def dataSet(self, type):
        if str(type) == 'comment':
            # comment,time,title,url
            p = r'Data/processFile/paper/dataSet/comment'
            return p
        elif str(type) == 'data':
            # meta{content,keywords,description},time,url
            p = r'Data/processFile/paper/dataSet/data'
            return p
        else:
            print('no relative type dataSet')
    
    def FinaldataSet(self, type):
        if str(type) == 'comment':
            # comment,time,title,url,properties
            p = r'Data/processFile/paper/dataSet/Finalcomment'
            return p
        elif str(type) == 'data':
            # meta{content,keywords,description},time,url,properties
            p = r'Data/processFile/paper/dataSet/Finaldata'
            return p
        else:
            print('no relative type dataSet')
            

class writePath:
    def allArticles(self,type):
        if str(type) == 'original':
            p = 'Data/processFile/paper/writeFolder/allArticles.txt'
            return p
        elif str(type) == 'fenci':
            p = 'Data/processFile/paper/writeFolder/allArticlesFenci.txt'
            return p
        else:
            print('no relative type dataSet')
            