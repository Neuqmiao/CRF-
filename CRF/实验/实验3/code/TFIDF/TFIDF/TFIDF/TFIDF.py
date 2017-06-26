# -*- encoding: gbk -*-

import os
import codecs
import math
import operator

def fun(filepath):#�����ļ����е������ļ��������ļ�list
    arr=[]
    for root,dirs,files in os.walk(filepath):
        for fn in files:
            arr.append(root+"\\"+fn)
    return arr

def wry(txt,path):#д��txt�ļ�
    f=codecs.open(path,'a','utf8')
    f.write(txt)
    f.close()
    return path

def read(path):#��ȡtxt�ļ���������list
    f=open(path,encoding="utf8")
    data=[]
    for line in f.readlines():
        data.append(line)
    return data

def toword(txtlis):#��һƬ���°��ա�/���и�ɴʱ�����list
    wordlist=[]
    alltxt=''
    for i in txtlis:
        alltxt=alltxt+str(i)
    ridenter=alltxt.replace('\n','')
    wordlist=ridenter.split('/')
    return wordlist

def getstopword(path):#��ȡͣ�ôʱ�
    swlis=[]
    for i in read(path):
        outsw=str(i).replace('\n','')
        swlis.append(outsw)
    return swlis

def getridofsw(lis,swlist):#ȥ�������е�ͣ�ô�
    afterswlis=[]
    for i in lis:
        if str(i) in swlist:
            continue
        else:
            afterswlis.append(str(i))
    return afterswlis

def freqword(wordlis):#ͳ�ƴ�Ƶ���������ֵ�
    freword={}
    for i in wordlis:
        if str(i) in freword:
            count=freword[str(i)]
            freword[str(i)]=count+1
        else:
            freword[str(i)]=1
    return freword

def corpus(filelist,swlist):#�������Ͽ�
    alllist=[]
    for i in filelist:
        afterswlis=getridofsw(toword(read(str(i))),swlist)
        alllist.append(afterswlis)
    return alllist

def wordinfilecount(word,corpuslist):#��������ôʵ��ĵ���
    count=0#������
    for i in corpuslist:
        for j in i:
            if word in set(j):#ֻҪ�ĵ����ָôʣ����������1�����������ü���
                count=count+1
            else:
                continue
    return count

def tf_idf(wordlis,filelist,corpuslist):#����TF-IDF,�������ֵ�
    outdic={}
    tf=0
    idf=0
    dic=freqword(wordlis)
    outlis=[]
    for i in set(wordlis):
         tf=dic[str(i)]/len(wordlis)#����TF��ĳ�����������г��ֵĴ���/�����ܴ���
         idf=math.log(len(filelist)/(wordinfilecount(str(i),corpuslist)+1))#����IDF��log(���Ͽ���ĵ�����/(�����ôʵ��ĵ���+1))
         tfidf=tf*idf#����TF-IDF
         outdic[str(i)]=tfidf
    orderdic=sorted(outdic.items(),key=operator.itemgetter(1),reverse=True)#���ֵ�����
    return orderdic

def befwry(lis):#д��Ԥ������listתΪstring
    outall=''
    for i in lis:
        ech=str(i).replace("('",'').replace("',",'\t').replace(')','')
        outall=outall+'\t'+ech+'\n'
    return outall

def main():
    swpath=r'H:\transfer\ʵ��3\���������ʵ��3_��Ϣ131_�����_19113106\������ͣ�ôʱ�.txt'
    swlist=getstopword(swpath)#get stop word list

    filepath=r'H:\transfer\ʵ��3\���������ʵ��3_��Ϣ131_�����_19113106\2015.1.16-2015.1.18(�˹��ִ�)'
    filelist=fun(filepath)#��ȡ�ļ��б�

    wrypath=r'H:\transfer\ʵ��3\���������ʵ��3_��Ϣ131_�����_19113106\TFIDF.txt'

    corpuslist=corpus(filelist,swlist)#�������Ͽ�

    outall=''

    for i in filelist:
        afterswlis=getridofsw(toword(read(str(i))),swlist)#��ȡÿһƪ�Ѿ�ȥ��ͣ�õĴʱ�
        tfidfdic=tf_idf(afterswlis,filelist,corpuslist)#����TF-IDF

        titleary=str(i).split('\\')
        title=str(titleary[-1]).replace('utf8.txt','')
        echout=title+'\n'+befwry(tfidfdic)
        print(title+' is ok!')
        outall=outall+echout
    print(wry(outall,wrypath)+' is ok!')

if __name__=='__main__':
    main()