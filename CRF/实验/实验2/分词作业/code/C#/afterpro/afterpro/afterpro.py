# -*- encoding: gbk -*-

import os
import codecs

def fun(filepath):
    arr=[]
    for root,dirs,files in os.walk(filepath):
        for fn in files:
            arr.append(root+"\\"+fn)
    return arr

def wry(lis,path):
    f=codecs.open(path,'a','utf8')#.encoding('utf16')
    for i in lis:
        f.write(str(i)+'\n')
    f.close()
    return path

def read(path):
    f=open(path,encoding="utf8")
    #count=0
    data=[]
    for line in f.readlines():
        data.append(line)
    return data

def chaPa(path):
    outpath=str(path).replace('人工分词19113106','人工分词19113106(utf8)').replace('.txt','utf8.txt').replace('pro','')
    return outpath

def pro(alis):
    outlis=[]
    for i in alis:
        ech=str(i)
        outlis.append(ech)
    return outlis

def bfwry(lis):
    alltxt=''
    for i in lis:
        alltxt=alltxt+str(i)
    return alltxt

def main():
    filepath=r"D:\校园\信息131\大三下\计算机检索\实验3\人工分词19113106"
    #path=r"D:\校园\信息131\大三下\计算机检索\分词作业\实验1shuchu\2015.1.16-2015.1.18\2015.1.17\2\2013年度中央预算执行审计等查出问题已整改1062亿多元after.txt"
    #wrypath=r"D:\校园\信息131\大三下\计算机检索\分词作业\testout.txt"
    #wrypath=r"D:\校园\信息131\大三下\计算机检索\分词作业\testout.txt"

    for i in fun(filepath):
        alis=read(str(i))
        outxt=pro(alis)
        outinfo=wry(alis,chaPa(str(i)))
        print(outinfo+" is ok!")
    '''outxt=pro(alis)
    outinfo=wry(outxt,wrypath)
    print(outinfo+" is ok!")'''

if __name__=='__main__':
    main()