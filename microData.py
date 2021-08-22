import os
import json
import pandas as pd

def txtToCsv(path):
    '''
    txt 写入CSV
    :param : 文件
    // 评论为0的值需要进行了手工剔除
    // 文章数小于10 ，情感值为1 ，需要手工剔除
    日期，文章数，文章分数，评论数，评论分数, 文章情感均值，评论情感均值
    
    ''' 
    # df = pd.read_csv(path,header=None,names = ['日期','文章数','文章分数','评论数','评论分数','文章情感均值','评论情感均值'])
    df = pd.read_csv(path,header=None,names = ['日期','文章数','评论数','评论总分值','评论情感值'])
    # df.to_csv('Final_comments_politic_v4.txt.csv',encoding = 'utf_8_sig')
    df.to_csv('wuhanDataPolitic.csv',index=False ,encoding = 'utf_8_sig')

def Txt2Csv(Txt_path, Csv_path):
    '''
    :param Txt_path: txt文件路径
    :param Csv_path: csv文件路径
    :return:
    '''
    with open(Txt_path, encoding='utf-8') as f:
        contents = []
        readlines = f.readlines()   # readlines是一个列表
        for i in readlines:
            line = i.strip().split(",")     # 去掉前后的换行符，之后按逗号分割开
            print(line)
            contents.append(line)   # contents二维列表
    df = pd.DataFrame(contents)

    # df.to_csv(Csv_path, header=False)           # 不添加表头
    try:
        df.columns = ['日期','URL','分类','情感值','评论内容']  # 添加表头
    except:
        print(os.error)
    df.to_csv(Csv_path, index=False ,header=False ,encoding = 'utf_8_sig')
    print("数据写入成功")
    
def findURL(url,FindName):
    with open(FindName,'r',encoding= 'utf-8') as fr:
        data = json.load(fr)
        for line in data:
            if str(url) == line['url']:
                # print(url,line['url'])
                return line['property']['number']



if __name__ =="__main__":
    Txt_path = r'/Users/xuanlongqin/Documents/data/covid-19/economicComment.txt'
    Csv_path = r'economicComment.csv'
    Txt2Csv(Txt_path, Csv_path)
    
    # path = '/Users/xuanlongqin/Documents/data/covid-19/wuhanDataPolitic.txt'
    # txtToCsv(path)
    
'''
    # commentPath = globalPath().dataSet('comment')
    # commentPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/processFile/paper/dataSet/sinaNews/comment'
    # FinalcommentPath = globalPath().FinaldataSet('comment')
    # FinalcommentPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/processFile/paper/dataSet/sinaNews/finalcomment'
    # 评论简表
    # metaPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/data'
    commentPath = r'/Users/xuanlongqin/Documents/data/covid-19/Data/news/dataSet/sinaNews/newcomment'

    print(commentPath)
    files= os.listdir(commentPath)
    files.sort()
    for file in files:
        fileName = commentPath + '/' + file
        # FindName = metaPath +'/' + file
        # print(fileName,metaPath)
        with open(fileName,'r',encoding='utf-8') as fr:
            data = json.load(fr)
            for line in data:
                # print(line)
                timeT = line['time']
                timeF = timeT.split(' ')[0]
                url = line['url']
                # num = findURL(url,FindName)
                c = line['comment']
                if len(c):
                    for comment in c:
                        senti = comment['sentiment']
                        if str(senti) == 'null':
                            print('sentiment is null')
                            continue
                        else:  
                            content = comment['content']
                            cfinal = content.replace('\n', '').replace('\r', '')
                            print(timeF,url,senti,cfinal) 
                            with open('AllComment_v4.txt','a+',encoding= 'utf-8') as fw:
                                fw.write( str(timeF) + ',' + str(url) + ',' + str(senti) + ',' + str(cfinal) + '\n')
                                fw.close()
                else:
                    continue
'''
        
            
'''
            获取文章简表
            for line in data:
                num = line['property']['number']
                timeT = line['time']
                timeF = timeT.split(' ')[0]
                url = line['url']
                classId = line['property']['class']
                if str(type(classId)) == "<class 'str'>":
                    c = classId
                elif str(type(classId)) == "<class 'list'>":
                    list2 = [str(i) for i in classId]
                    c = '/'.join(list2)
                else:
                    c = 'error'
                
                senti = line['sentiment']
                title = line['title']
                content = line['meta']['content']
                
                # print(num,timeT,url,c,senti,title)
                with open('AllContent.txt','a+',encoding= 'utf-8') as fw:
                    fw.write(str(num) + ',' + str(timeF) + ',' + str(url) + ',' + str(c) + ',' + str(senti) + ',' + str(title) + '\n')
                    # fw.write(str(num) + ',' + str(timeF) + ',' + str(url) + ',' + str(c) + ',' + str(senti) + ',' + str(title) + ',' + str(content) + '\n')
                    fw.close()
                    
                '''
    # Txt2Csv('AllContent.txt', 'AllContent.csv')
        