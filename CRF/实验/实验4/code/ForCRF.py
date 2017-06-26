import time
import codecs
import os
import random

def fun(filepath):#遍历文件夹中的所有文件，返回文件list
    arr=[]
    for root,dirs,files in os.walk(filepath):
        for fn in files:
            arr.append(root+"\\"+fn)
    return arr

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
        if line =='\n':
            continue
        if line =='':
            continue
        else:
            data.append(line)
    return data

def basket(lis):#遍历二维数组，将所有的文献放到同一个篮子里
    basketlis=[]
    for i in lis:
        for j in i:
            repla=str(j).strip().replace(' ','').replace('　　','').replace('！','！$').replace('？','？$').replace('；','；$').replace('。','。$')
            spl=repla.replace('。$/”','。/”$').replace('！$/”','！/”$').replace('？$/”','？/”$')
            if spl=='':
                continue
            if spl=='/':
                continue
            if spl=='\n':
                continue
            else:
                basketlis.append(spl)
    return basketlis

def splisen(lis):
    splis=[]
    for i in lis:
        echsen=str(i).split('$')
        for j in echsen:
            if str(j)=='':
                continue
            if str(j)=='/':
                continue
            else:
                splis.append(str(j))
    return splis

def randomlis(lis):
    random.shuffle(lis)
    return lis

def perallegt(lis):
    txtlen=len(lis)
    getlen=int(txtlen*0.8)
    egtlis=[]
    for i in lis[0:getlen+1]:
        egtlis.append(str(i))
    return egtlis

def peralltwe(lis):
    txtlen=len(lis)
    getlen=int(txtlen*0.8)
    twelis=[]
    for i in lis[getlen+1:]:
        twelis.append(str(i))
    return twelis

def protoword(lis):
    allword=[]
    for i in lis:
        echsen=str(i).split('/')
        for j in echsen:
            allword.append(str(j))
        #allword.append('#')
    return allword

def inbce(lis):
    outtxt=[]
    for i in lis:
        if str(i)=='':
            outtxt.append(str(i))
        else:
            if len(str(i))==1:
                outtxt.append(str(i)+'\tBE')
            elif len(str(i))==2:
                outtxt.append(str(i)[0]+'\tB')
                outtxt.append(str(i)[1]+'\tE')
            elif len(str(i))>2:
                outtxt.append(str(i)[0]+'\tB')
                for j in str(i)[1:-1]:
                    outtxt.append(str(j)+'\tC')
                outtxt.append(str(i)[-1]+'\tE')
    return outtxt

def main():
    systime=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    #filepath=r'F:\刘睿伦\实验3\2015.1.16-2015.1.18(人工分词)'
    file=r'C:\Users\AlanConstantine\Desktop\19113103'
    wrypathegt=r'C:\Users\AlanConstantine\Desktop\train'+systime+'.txt'
    wrypathtwe=r'C:\Users\AlanConstantine\Desktop\test'+systime+'.txt'
    allis=[]
    for i in fun(file):
        echtxt=read(str(i))
        allis.append(echtxt)
    baslisegt=inbce(protoword(perallegt(randomlis(splisen(basket(allis))))))
    baslistwe=inbce(protoword(peralltwe(randomlis(splisen(basket(allis))))))
    print(wry(baslisegt,wrypathegt)+' is ok!')
    print(wry(baslistwe,wrypathtwe)+' is ok!')
    #for i in baslis:
        #print(str(i))

if __name__=='__main__':
    main()
