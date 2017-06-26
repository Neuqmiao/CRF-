#! python3
# -*- coding: utf-8 -*-
import os


def lead_in_stop_words(stop_words_name):
    keywords = []
    with open("%s.txt" % stop_words_name, "r", encoding='utf8') as f:
        data = f.readlines()
        for line in data:
            keywords.append(line.replace('\n', '').replace('\ufeff', ''))
    return keywords


def read_essay(path):
    with open(path, encoding='utf8') as f:
        essay = f.read()
    return essay


def reverse_match(essay, essay_name, data):
    words = []
    output = ""
    len_essay = len(essay)
    maxlen = 8

    while len_essay >= maxlen:
        truncation = essay[-maxlen:len_essay]

        for i in range(maxlen+1, 1, -1):
            truncation = truncation[-i:]
            if (truncation in data) or (i == 1):
                len_essay -= i
                essay = essay[:len_essay]
                words.append(truncation.replace('\n', ''))
                output = truncation + "/" + output

                break

    while len_essay:
        truncation = essay

        for i in range(len_essay+1, 1, -1):
            truncation = truncation[-i:]
            if (truncation in data) or (i == 1):
                len_essay -= i
                essay = essay[:len_essay]
                words.append(truncation.replace('\n', ''))
                output = truncation + "/" + output

                break

    # with open("res/%s" % essay_name, "w") as f:
    #     f.write(output)
    print(output)
    return words


def count_words(words, essay_name):
    words_set = set(words)
    for word in words_set:
        count = words.count(word)
        with open("res/统计词频_%s.txt" % essay_name.replace('.txt', ''), "a") as f:
            f.write(word + "\t" + str(count))


# def main():
#     stop_words_list = lead_in_stop_words('中文停用词库')
#     for file in os.listdir(os.getcwd()):
#         print(file)
#         if file.endswith('.txt') and file != '中文停用词库.txt':
#             with open(file, 'r', encoding='utf8') as f:
#                 paper = f.read()
#                 frequence = reverse_match(paper, file, stop_words_list)
#                 print(frequence)
#                 count_words(frequence, file)
#         break

if __name__ == '__main__':
    res = lead_in_stop_words("中文停用词库")
    print(res)
    article = read_essay(r'2012.11.17北京：习总书记在十八届中共中央政治局第一次集体学习时的讲话.txt')
    reverse_match(article, '分词后文章', res)