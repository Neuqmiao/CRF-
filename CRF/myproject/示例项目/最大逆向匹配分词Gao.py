# -*- coding: utf-8 -*-
# 最大逆向匹配分词算法
import xlrd

def read_xlsx(path):
    x1 = xlrd.open_workbook(path)
    sheet1 = x1.sheets()[0]
    
    col_2 = sheet1.col_values(1)
    return col_2


def read_essay(path):
    with open(path, encoding='utf8') as f:
        essay = f.read()    
    return essay


def reverse_match(essay,essay_name,data1,data2):#data为语料库
    length = 8
    len_essay = len(essay)
    new_essay = ''#记录插入/后的文章
    words_list = [] #记录分出的词
    
    while len_essay >= length:
        strn = essay[-length:len_essay]      
        
        for i in reversed(range(1,length + 1)):                
            strn = strn[-i:]
            if (strn in data1) or(strn in data2) or (i ==1):       
                len_essay -= i
                essay = essay[:len_essay]
                words_list.append(strn)
                new_essay = strn + '/' + new_essay 
                break
    while len_essay:
        strn = essay
        for i in reversed(range(1,len_essay +1)):
            strn = strn[-i:]
            if (strn in data1) or(strn in data2) or (i ==1):            
                len_essay -= i
                essay = essay[:len_essay]
                words_list.append(strn)
                new_essay = strn + '/' + new_essay
                break
            
    with open(str(essay_name) +'.txt','w') as f:
        f.write(new_essay) 
    
    return words_list


def count_words(words_list):
    words_set = set(words_list)
    for word in words_set:
        num = words_list.count(word)
        with open("统计词频.txt",'a') as f:
            f.write(word + '\t' + str(num) +'\n')


def main():  
    data1 = read_xlsx(r'stopwords.xlsx')
    data2 = read_xlsx(r'words.xlsx')
    
    essay = read_essay(r'2012.11.17北京：习总书记在十八届中共中央政治局第一次集体学习时的讲话.txt')
    words_list = reverse_match(essay,'分词后文章',data1,data2)
    count_words(words_list) 
 
if __name__ =='__main__':
    main()

