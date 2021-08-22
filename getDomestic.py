import os
import json

from urllib.parse import urlparse
 

def findArticles(data,outPath):
    for line in data:
        url = line['url']
        _url = urlparse(url)
        url_path = _url.path
        url_key = url_path.split('/')[1]
        
        if str(url_key) == 'w' or str(url_key) == 'world':
            try:
                jsonStr = json.dumps(line,indent=4,ensure_ascii=False)
                with open(outPath,'a+',encoding= 'utf-8') as fw:
                    fw.write(jsonStr + ',' + '\n')
                    fw.close()
            except:
                print('content error')
        else:
            continue
        
def findComments(data,outCommentPath):
    for line in data:
        url = line['url']
        _url = urlparse(url)
        url_path = _url.path
        url_key = url_path.split('/')[1]
        
        if str(url_key) == 'w' or str(url_key) == 'world':
            try:
                jsonStr = json.dumps(line,indent=4,ensure_ascii=False)
                with open(outCommentPath,'a+',encoding= 'utf-8') as fw:
                    fw.write(jsonStr + ',' + '\n')
                    fw.close()
            except:
                print('comment error')
        else:
            continue


if __name__ == '__main__':
    SinaNewsMetaPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/data'
    domesticData = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/internationalData/data'
    
   #  FinalCommentClass = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/FinalCommentClass'
   # outCommentPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/internationalData/comment'
    
    files= os.listdir(SinaNewsMetaPath)
    files.sort()
    
    for file in files:
        fileName = SinaNewsMetaPath + '/' + file
        # fileName = FinalCommentClass + '/' + file
        outPath = domesticData + '/' + file
        with open(fileName,'r',encoding='utf-8') as fr:
            data = json.load(fr)
            findArticles(data,outPath)
            #findComments(data,outPath)
            
    