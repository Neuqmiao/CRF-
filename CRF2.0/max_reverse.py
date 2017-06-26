#! python3
# -*- coding: utf-8 -*-
import xlrd
from datetime import datetime


def vocabulary(path):
    """从excel表格获得词表"""
    x1 = xlrd.open_workbook(path)
    sheet1 = x1.sheets()[0]

    col_2 = sheet1.col_values(1)
    return col_2[1:]


def read_essay():
    with open('test.txt', 'r', encoding='utf8') as f:
        content = f.read().strip()
        return content


def max_reverse(essay, essay_name, stop_words_vocabulary, words_vocabulary):
    """最大逆向匹配分词算法"""
    essay_length = len(essay)  # 一定要将空白符给去掉然后得出文章长度
    new_essay = ''
    parts = []

    while essay_length >= 8:  # 当文章长度大于8时
        cut = essay[-8:essay_length]  # 切出长度为8的字符串
        """开始对子串进行处理"""
        for i in range(8, 0, -1):
            inside_cut = cut[-i:]  # 对子串进行切割
            if (inside_cut in stop_words_vocabulary) or (inside_cut in words_vocabulary) or (i == 1):
                new_essay = inside_cut + '/' + new_essay  # 形成带斜杠的文章
                essay_length -= i
                essay = essay[:essay_length]  # 只要找到一个词就将文章长度减小
                parts.insert(0, inside_cut)  # 不断将找到的词语插入到列表中
                break

    while 0 < essay_length < 8:  # 当文章长度已经减小到小于8时
        for i in range(essay_length, 0, -1):
            inside_cut = essay[-i:]
            inside_cut_length = len(inside_cut)
            if (inside_cut in stop_words_vocabulary) or (inside_cut in words_vocabulary) or inside_cut_length == 1:
                new_essay = inside_cut + '/' + new_essay  # 形成带斜杠的文章
                essay_length -= i
                essay = essay[:essay_length]  # 只要找到一个词就将文章长度减小
                parts.insert(0, inside_cut)  # 不断将找到的词语插入到列表中
                break

    with open('slash_%s.txt' % essay_name, 'w') as f:
        f.write(new_essay)

    return parts


def combine():
    data1 = vocabulary('stopwords.xlsx')
    data2 = vocabulary('words.xlsx')
    essay = read_essay()
    print(datetime.now())
    result = max_reverse(essay, 'test', data1, data2)
    print(datetime.now())


if __name__ == '__main__':
    combine()
