"""
Created on Fri June 17 19:30:34 2016

@author: AlanConstantine(Liu RuiLun 19113106)
"""

import time
import os
import codecs

global bp
global br
global bf

global ep
global er
global ef

global cp
global cr
global cf

global bep
global ber
global bef

bp=0
br=0
bf=0

ep=0
er=0
ef=0

cp=0
cr=0
cf=0

bep=0
ber=0
bef=0

def wry(lis,path):#写入txt文件
    f=codecs.open(path,'a','utf8')
    for i in lis:
        f.write(str(i)+'\n')
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
    return charr

def precision(lis,bce):#准确率
    numerator=0#分子
    denominator=0#分母
    for i in lis:
        if str(i[2])==bce:
            if str(i[2])==str(i[1]):
                numerator=numerator+1
        if str(i[2])==bce:
            denominator=denominator+1
    return numerator/denominator

def recall(lis,bce):#召回率
    numerator=0#分子
    denominator=0#分母
    for i in lis:
        if str(i[2])==bce:
            if str(i[2])==str(i[1]):
                numerator=numerator+1
        if str(i[1])==bce:
            denominator=denominator+1
    return numerator/denominator
    

def HarF(p,r):#F值
    return p*r*2/(p+r)

def countB(lis):
    p=precision(lis,'B')
    r=recall(lis,'B')
    global bp
    global br
    global bf
    bp=p
    br=r
    bf=HarF(p,r)
    return 'B:\n'+'\tPrecision:'+str(p)+'\n\tRecall:'+str(r)+'\n\tF-measure:'+str(bf)

def countBE(lis):
    p=precision(lis,'BE')
    r=recall(lis,'BE')
    global bep
    global ber
    global bef
    bep=p
    ber=r
    bef=HarF(p,r)
    return 'BE:\n'+'\tPrecision:'+str(p)+'\n\tRecall:'+str(r)+'\n\tF-measure:'+str(bef)

def countE(lis):
    p=precision(lis,'E')
    r=recall(lis,'E')
    global ep
    global er
    global ef
    ep=p
    er=r
    ef=HarF(p,r)
    return 'E:\n'+'\tPrecision:'+str(p)+'\n\tRecall:'+str(r)+'\n\tF-measure:'+str(ef)

def countC(lis):
    p=precision(lis,'C')
    r=recall(lis,'C')
    global cp
    global cr
    global cf
    cp=p
    cr=r
    cf=HarF(p,r)
    return 'C:\n'+'\tPrecision:'+str(p)+'\n\tRecall:'+str(r)+'\n\tF-measure:'+str(cf)

def aver():
    return 'Average:\n'+'\tPrecision:'+str((bp+bep+ep+cp)/4)+'\n\tRecall:'+str((br+ber+er+cr)/4)+'\n\tF-measure:'+str((bf+bef+ef+cf)/4)

def main():
    systime=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
	
    txtpath=r'F:\output.txt'
    wrypath=r'F:\RPF'+systime+'.txt'

    txtlis=chaArry(read(txtpath))

    outinfo=[]
    outinfo.append(countB(txtlis))
    outinfo.append(countBE(txtlis))
    outinfo.append(countE(txtlis))
    outinfo.append(countC(txtlis))
    outinfo.append(aver())
    
    print(wry(outinfo,wrypath))

if __name__=='__main__':
    main()
