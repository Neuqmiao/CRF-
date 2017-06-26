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
    f=codecs.open(path,'a','utf8')#.encoding('utf16')
    f.write(lis)
    f.close()
    return path

def splword(txt):
    seg_list = jieba.cut(txt,cut_all = False)
    aft="/ ".join(seg_list)
    return aft

def main():
    filepath=r"F:\信息检索 2016-05\19113126"
    uipath=unicode(filepath,"utf8")
    lis=fun(uipath)
    allin=""
    for i in lis:
        alltxt=read(i)
        outpath=i.replace(".txt","after.txt").replace("19113126","19113126fc")
        #upath=unicode(outpath,"utf8")
        for j in alltxt:
            allin=allin+str(j)
        outtxt=splword(allin)
        allin=''
        outinfor=wry(outtxt,outpath)
        print outinfor,"is ok!"
    print "Is over!!!"

if __name__=='__main__':
    main()