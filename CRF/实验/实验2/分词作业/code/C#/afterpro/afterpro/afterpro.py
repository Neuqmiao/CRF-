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
    outpath=str(path).replace('�˹��ִ�19113106','�˹��ִ�19113106(utf8)').replace('.txt','utf8.txt').replace('pro','')
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
    filepath=r"D:\У԰\��Ϣ131\������\���������\ʵ��3\�˹��ִ�19113106"
    #path=r"D:\У԰\��Ϣ131\������\���������\�ִ���ҵ\ʵ��1shuchu\2015.1.16-2015.1.18\2015.1.17\2\2013�������Ԥ��ִ����ƵȲ������������1062�ڶ�Ԫafter.txt"
    #wrypath=r"D:\У԰\��Ϣ131\������\���������\�ִ���ҵ\testout.txt"
    #wrypath=r"D:\У԰\��Ϣ131\������\���������\�ִ���ҵ\testout.txt"

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