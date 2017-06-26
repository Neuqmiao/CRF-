# -*- coding: utf-8 -*-
# 最大逆向匹配分词算法
import os

def lead_in_stop_words(stop_words_name):
    keywords = []
    with open("%s.txt" % stop_words_name, "r", encoding='utf8') as f:
        data = f.readlines()
        for line in data:
            keywords.append(line.replace('\n', '').replace('\ufeff', ''))
    return keywords


def read_essay(path):
    with open(path, 'r', encoding='utf8') as f:
        essay = f.read()
    return essay


def reverse_match(essay, essay_name, data):  # data为语料库
    length = 8
    len_essay = len(essay)
    new_essay = ''  # 记录插入/后的文章
    words_list = []  # 记录分出的词

    while len_essay >= length:
        strn = essay[-length:len_essay]

        for i in reversed(range(1, length + 1)):
            strn = strn[-i:]
            if (strn in data) or (i == 1):
                len_essay -= i
                essay = essay[:len_essay]
                words_list.append(strn)
                new_essay = strn + '/' + new_essay
                break
    while len_essay:
        strn = essay
        for i in reversed(range(1, len_essay + 1)):
            strn = strn[-i:]
            if (strn in data) or (i == 1):
                len_essay -= i
                essay = essay[:len_essay]
                words_list.append(strn)
                new_essay = strn + '/' + new_essay
                break

    with open("res/%s" % (str(essay_name) + '.txt'), 'w', encoding='utf8') as f:
        f.write(new_essay)

    return words_list


def count_words(words_list, data):  # 通过交叉对比文章与停用词表，来观察文章有多少水分
    print(data)
    statistics = {}
    words_set = set(words_list)
    for word in words_set:
        for stop_word in data:
            if word == stop_word:
                num = words_list.count(word)
                statistics[word] = num
                # with open("统计词频.txt", 'a') as f:
                #     f.write(word + '\t' + str(num) + '\n')
    print(statistics)
    for key, value in statistics.items():
        with open("正确统计词频.txt", "a") as f:
            f.write(key + '\t' + str(value) + '\n')


def main():
    # data = read_essay(r'中文停用词库.txt')
    data1 = lead_in_stop_words(r'')
    data2 = lead_in_stop_words()
    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt') and file != '中文停用词库.txt':
            essay = read_essay(file)
            words_list = reverse_match(essay, '分词后文章_%s' % file.replace('.txt', ''), data)
    # essay = read_essay(r'2012.11.17北京：习总书记在十八届中共中央政治局第一次集体学习时的讲话.txt')
    # words_list = reverse_match(essay, '分词后文章', data)
    # count_words(words_list, data)


if __name__ == '__main__':
    main()

