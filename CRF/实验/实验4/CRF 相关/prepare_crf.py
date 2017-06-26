# -*- coding: utf-8 -*-
"""
根据CRF对训练文本的格式要求，将标注好的预料转变成可以对应的格式
"""

import os
import re


def traverse_dir(tra_dir):
    # check tra_dir not None or ''

    list_files = list()
    list_file_name = list()
    list_dirs = os.walk(tra_dir)

    for root, dirs, files in list_dirs:
        #print(files)
        for f in files:
            list_files.append(os.path.join(root, f))
            list_file_name.append(f)

    return list_files


def tagging(word):
    l = list()
    if len(word) > 2:
        for i in range(0, len(word)):
            if i == 0:
                l.append(word[i] + '\t' + 'B')
            elif i > 0 and i != (len(word) - 1):
                l.append(word[i] + '\t' + 'C')
            elif i == (len(word) - 1):
                l.append(word[i] + '\t' + 'E')
    elif len(word) == 2:
        for i in range(0, len(word)):
            if i == 0:
                l.append(word[i] + '\t' + 'B')
            elif i == 1:
                l.append(word[i] + '\t' + 'E')
    elif len(word) == 1:
        l.append(word + '\t' + 'BE')
    return l


def process_texts_for_crf_format(list_files):
    '''
    process the raw texts (which have been tokenized and taged)
    :param list_texts:
    :return:
    '''
    list_sen = ['。', '！', '？', '?', ';']
    list_out = list()
    for doc in list_files:
        text = ''
        #print(doc)
        for line in open(doc, encoding='utf-8', errors=None):
            if line.strip() == '':
                continue
            text += line.strip('nr').strip()
            
        # used for processing corpus of “人民日报”
#        for token in text.split():
#            if token.strip() == '':
#                continue
#            # print(doc + '\t' + token)
#            splits = token.split('/')
#            if len(splits) == 1:
#                continue
#            word = token.split('/')[0]
#            tag = token.split('/')[1]
#
#            # if len(re.findall('[0-9]|[A-z]', word)) > 0:
#            #     continue
#            l_tag = tagging(word, tag)
#            list_out.extend(l_tag)
#            if word in list_sen:
#                list_out.append('')

        for token in text.split('/'):
            if token.strip() == '':
                print('----------WARNING: the whitespace is splited!---------')
                continue

            list_out.extend(tagging(token.strip()))
            if token in list_sen:
                list_out.append('')

    return list_out


def choose_random_crf(list_crf):
    '''
    random the content of the file for processing. Take the all sentence as the whole bulk
    :param list_crf:
    :return:
    '''
    list_sen = list()
    list_tmp = list()
    for item in list_crf:
        if item == '':
            list_sen.append(list_tmp)
            list_tmp = list()
            continue
        list_tmp.append(item)

    import random
    random.shuffle(list_sen)

    return list_sen


if __name__ == '__main__':
    list_files = traverse_dir(r'D:\Post-DOC\课程\信息检索 2016-05\1914211')
    list_out = process_texts_for_crf_format(list_files)
    list_sen = choose_random_crf(list_out)

    w_f = open(r'D:\Post-DOC\课程\信息检索 2016-05\实验内容\2 - 分词作业\CRF train.txt', 'w', encoding='utf-8')
    for item in list_sen:
        print(item)
        for tag in item:
            w_f.write(tag + '\n')
        w_f.write('\n')
    w_f.close()

    # w_f = open(dir + 'test.%s.txt' % str(f), 'w', encoding='utf-8')
    # for item in test_instances:
    #     for tag in item:
    #         w_f.write(tag + '\n')
    #     w_f.write('\n')
    # w_f.close()


