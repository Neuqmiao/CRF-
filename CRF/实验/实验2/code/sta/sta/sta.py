# -*- coding:utf-8 -*-
import os
import codecs

def fun(filepath):
    arr=[]
    for root,dirs,files in os.walk(filepath):
        for fn in files:
            arr.append(root+"\\"+fn)
    return arr

def read(path):
    f=open(path,encoding="utf8")
    #count=0
    data=[]
    for line in f.readlines():
        data.append(line)
    return data

def wry(lis,path):
    count=0
    f=codecs.open(path,'a','utf16')#.encoding('utf16')
    for i in lis:
        f.write(str(i)+'\n')
        count=count+1
    f.close()
    return count

def main():
    filepath=r'D:\У԰\��Ϣ131\������\���������\ʵ��1shuchu2\2015.1.16-2015.1.18'
    for i in fun(filepath):
        print(i)

if __name__=='__main__':
    main()