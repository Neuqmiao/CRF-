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
    return path

def freQ(data):
    dic={}
    for i in data:
        eachline=str(i).replace(' ','').replace('\n','').replace('　','')
        #allword=eachline.split('/')
        for j in eachline:
            if j=='':
                continue
            else:
                if j in dic:
                    co=dic[j]
                    dic[j]=co+1
                else:
                    dic[j]=1
    relis=[]
    count=0
    for k in dic:
        count=count+1
        relis.append(str(count)+'\t'+str(k)+'\t'+str(dic[k]))
    return relis

def chaPa(path):
    outpath=str(path).replace('19113124','19113124out').replace('.txt','count.txt')
    return outpath
    
                
def main():
    filepath=r'C:\Users\AlanConstantine\Desktop\19113124'
    for i in fun(filepath):
        lis=read(i)
        coinfor=freQ(lis)
        outpath=chaPa(i)
        infor=wry(coinfor,outpath)
        print(infor+' is ok!')
    print('Is over!!!')

if __name__=='__main__':
    main()
