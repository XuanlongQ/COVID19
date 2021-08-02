# -*- coding: utf-8 -*-
import jieba.posseg as pseg
import json
import os

from snownlp import SnowNLP



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
    
def cutwords(s):
    cutstr = ''
    seg_list = pseg.cut(s)
    for w in seg_list:
        if w.flag == 'n' or w.flag == 'v' or w.flag == 'y':
            cutstr =  cutstr + w.word
        else:
            pass            
    return cutstr

def cal(conts):
    num = 0
    senti = 0
    for content in conts:
        proWords = cutwords(content)
        score = sentimentFunc(proWords)
        print(num,proWords,score)
        
        senti  = senti + score
        num = num + 1
    finalsenti = senti/num
    return finalsenti


    
if __name__ == '__main__':    
    commentPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/comment'
    newFinalcomment = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/newFinalcomment'
    
    # 全部新闻文章分词
    files= os.listdir(commentPath)
    files.sort()
    for file in files:
        print(file)
        fileName = commentPath + '/' + file
        FindName = newFinalcomment +'/' + file
        print(fileName)
        print(FindName)  
    
        with open(fileName,'r', encoding = 'utf-8' ) as fr:
            data = json.load(fr)
            for line in data:
                d = line['comment']
                if len(d):
                    for comment in d:
                        c = comment['content']
                        score = sentimentFunc(c)
                        # print(c,score)
                        if score:
                            comment['sentiment']= score
                            # print(comment)
                        else:
                            continue
                else:
                    pass
                    
                    
                try:
                    json_str = json.dumps(line,indent=4,ensure_ascii=False)
                    with open(FindName, 'a+') as json_file:
                        json_file.write(json_str+',' +'\n')
                except:
                    print('write error') 
          
        
    # conts = content.split('。')[:-1]
    # final = cal(conts)
    # print(final)

    
    
        


