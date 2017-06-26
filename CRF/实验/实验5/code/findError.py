"""
Created on Fri June 17 22:47:18 2016

@author: AlanConstantine(Liu RuiLun 19113106)
"""

import time
import os
import codecs

def wry(lis,path):#写入txt文件
    f=codecs.open(path,'a','utf8')
    for i in lis:
        for j in i:
            f.write(str(j)+'\n')
        f.write('------------\n')
    f.close()
    return path

def read(path):#读取txt文件，并返回list
    f=open(path,encoding="utf8")
    data=[]
    for line in f.readlines():
        data.append(line)
    return data

def chaArry(lis):
    charr=[]
    for i in lis:
        if str(i)=='':
            continue
        else:
            echline=str(i).replace('\n','').split('\t')
            if len(echline)==3:
                charr.append(echline)
            else:
                charr.append(str(i)+'$')
    return charr

def putall(lis):
    alltxt=''
    for i in lis:
        if len(i)==1:
            alltxt=alltxt+str(i)
        else:
            echline=''
            for j in i:
                echline=echline+str(j)+'\t'
            alltxt=alltxt+echline+'&'
        senlis=alltxt.split('$')
    return senlis

def findError(lis):
    erolis=[]
    for i in lis:
        echsen=[]
        erosen=''
        echword=str(i).replace('\t&','&').split('&')
        for j in echword:
            ech=str(j).split('\t')
            if len(ech)==3:
                if str(ech[1])!=str(ech[2]):
                    #erosen=erosen+str(ech[0])+'\t'+str(ech[1])+'\t'+str(ech[2])+'\tError'
                    echsen.append(str(ech[0])+'\t'+str(ech[1])+'\t'+str(ech[2])+'\tError')
                else:
                    #erosen=erosen+str(ech[0])+'\t'+str(ech[1])+'\t'+str(ech[2])
                    echsen.append(str(ech[0])+'\t'+str(ech[1])+'\t'+str(ech[2]))
        for k in echsen:
            if 'Error' in str(k):
                if echsen in erolis:
                    continue
                else:
                    erolis.append(echsen)
        #if 'Error' in erosen:
            #erolis.append(erosen)
    #seterror=set(erolis)
    return erolis
                    
def main():
    systime=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
	
    txtpath=r'F:\output.txt'
    wrypath=r'F:\finderror'+systime+'.txt'

    #findErr(chaArry(read(txtpath)))
    #print(wry(chaArry(read(txtpath)),wrypath),'is ok!')
    print(wry(findError(putall(chaArry(read(txtpath)))),wrypath),'is ok!')

if __name__=='__main__':
    main()
