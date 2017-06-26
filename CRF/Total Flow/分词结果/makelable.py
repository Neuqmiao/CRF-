#! python3
# -*- coding: utf-8 -*-
"""先打乱句子，根据中文四个标点符号（。！？；）来分句子，然后用shuffle进行乱序处理，将句子竖型排列，
句子与句子保留标点符号并加上\n,然后进行打标签处理，如果是在data里面的词进行BCE, BME处理，如果不在data里面，
打标签为N, 同时应该抽出90%的句子，让机器去学习，剩下10%的句子让机器去模拟出结果，如果遇到109个句子，先将100个句子等分成10份，
然后再将剩下的9个句子均分成9份加到前面9份之中，相当于（11，11，11，11，11，11，11，11，11，10）其实最科学的方法是:将所有句子等分成10份，
然后(语料1  语料2-10)(语料2 语料1+语料3-10)以此类推，分成10个文件夹让机器分别去学习，还是90%语句去学习，剩下10%去模拟结果"""
import os
import xlrd
import random


def chaos():  # 进行句子乱序排列
    total_string = ''
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.txt'):
            with open(filename, 'r') as f:
                data = f.read()
                total_string += data
    new_string = total_string.replace('\n', '').replace('。', '。$').replace('；', '；$').replace('！', '！$').replace('？', '？$')
    all_content = new_string.split('$')
    print(all_content)
    print(len(all_content))
    random.shuffle(all_content)
    print(all_content)
    length = len(all_content)
    if length % 10 == 0:
        upper = int(length / 10) * 9
        training_content = all_content[0:upper]  # 机器学习训练语句 90%
        simulate_content = all_content[upper:-1] # 机器出结果语句 10%
    else:  # 当不能被整除时
        remainder = length % 10
        upper = int((length - (length % 10)) / 10) * 9 + remainder
        training_content = all_content[0:upper]   # 当不能整除时，机器学习训练语句 90%以上
        simulate_content = all_content[upper:-1]  # 机器学习出结果语句 10%以下
    return training_content, simulate_content


def read_xlsx(path):
    x1 = xlrd.open_workbook(path)
    sheet1 = x1.sheets()[0]

    col_2 = sheet1.col_values(1)
    return col_2


def make_label(chaos_list, data):
    res = []
    for sentence in chaos_list:
        words = sentence.split('/')
        for word in words:
            if word in data:
                if len(word) == 1:
                    add = word + '\t' + 'BE\n'
                    res.append(add)
                    # if word == '。' or word == '？' or word == '！' or word == '；':
                    #     res.append('\n')
                elif len(word) == 2:
                    add1 = word[0] + '\t' + 'B\n'
                    add2 = word[1] + '\t' + 'E\n'
                    res.append(add1)
                    res.append(add2)
                elif len(word) > 2:
                    add1 = word[0] + '\t' + 'B\n'
                    res.append(add1)
                    for middle in word[1:-1]:
                        addm = middle + '\t' + 'C\n'
                        res.append(addm)
                    add2 = word[-1] + '\t' + 'E\n'
                    res.append(add2)
            else:
                for i in word:
                    add = i + '\t' + 'N\n'
                    res.append(add)
                if len(word) == 1:
                    if word == '。' or word == '？' or word == '！' or word == '；':
                        res.append('\n')
    return res


if __name__ == '__main__':
    training, simulate = chaos()
    print('@@@')
    print(training)
    print(simulate)
    print('@@@')
    # corpus = read_xlsx(r'words.xlsx')  # 词库
    # training_save_format = ''.join(make_label(training, corpus))
    # simulate_save_format = ''.join(make_label(simulate, corpus))
    # with open('training.txt', 'w') as f:
    #     f.write(training_save_format)
    # with open('simulate.txt', 'w') as f:
    #     f.write(simulate_save_format)


