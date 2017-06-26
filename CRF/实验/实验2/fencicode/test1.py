# -*- coding:utf8 -*-
import jieba
import os
import codecs

def fun(filepath):
    arr=[]
    for root,dirs,files in os.walk(filepath):
        for fn in files:
            arr.append(root+"\\"+fn)
    return arr

def read(path):
    f=open(path)
    #count=0
    data=[]
    for line in f.readlines():
        data.append(line)
    return data

def wry(lis,path):
    count=0
    #uipath=unicode(path,'utf16')
    f=codecs.open(path,'a','utf16')#.encoding('utf16')
    f.write(lis)
    f.close()
    return path

def splword(txt):
    seg_list = jieba.cut(txt,cut_all = False)
    aft="/ ".join(seg_list)
    return aft

def main():
    filepath=r"D:\校园\信息131\大三下\计算机检索\实验1shiyan\2015.1.16-2015.1.18"
    uipath=unicode(filepath,"utf8")
    lis=fun(uipath)
    allin=""
    for i in lis:
        alltxt=read(i)
        outpath=i.replace(".txt","after.txt").replace("shiyan","shuchu")
        #upath=unicode(outpath,"utf8")
        for j in alltxt:
            allin=allin+str(j)
        outtxt=splword(allin)
        outinfor=wry(outtxt,outpath)
        print outinfor,"is ok!"
    print "Is over!!!"

if __name__=='__main__':
    main()
