# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 10:08:09 2016
输出TF-IDF值前100的词
@author: Administrator
"""

import os
from collections import OrderedDict
import math


# 获取所有文件
def traverse_dir(tra_dir):
    # check tra_dir not None or ''

    list_files = list()
    list_file_name = list()
    list_dirs = os.walk(tra_dir)
    for root, dirs, files in list_dirs:
        for f in files:
            list_files.append(os.path.join(root, f))
            list_file_name.append(f)

    return list_files


def extract_title(doc_file_name):
    return doc_file_name.split('.')[0].split('\\')[-1]


def num_docs_containing(word, list_of_tokens):
    count = 0
    for tokens in list_of_tokens:
        if tokens.count(word) > 0:
            count += 1
    return 1 + count
    

def tokenize(line):
    tokens = list()
    for item in line.split('/'):
        item = item.strip()
        tokens.append(item)
    return tokens
    

def prepare_labeled_tokens(list_texts):
    labeled_doc_tokens = list()
    for doc in list_texts:
        temp_line = ''
        for line in open(doc, encoding='utf-8'):
            line = line.strip()
            if line == '': 
                continue
            temp_line += line + '  '

        label = extract_title(doc)
        tokens = tokenize(temp_line)
        labeled_doc_tokens.append((label, tokens))

    return labeled_doc_tokens


def tf(word, doc_tokenized):
    return 1 + math.log(doc_tokenized.count(word)) 


def idf(labeled_doc_tokens):
    dict_idf = dict()
    
    set_all_tokens = set([token for (doc, tokens) in labeled_doc_tokens for token in tokens])
    list_tokens = [tokens for (doc, tokens) in labeled_doc_tokens]
    for tkn in set_all_tokens:
        # contains_token = map(lambda doc: tkn in doc, list_tokens)
        dict_idf[tkn] = round(
            1 + math.log(len(labeled_doc_tokens) / num_docs_containing(tkn, list_tokens)), 2)
    return dict_idf


def tfidf(doc_tokens):
    doc_features = list()
    
    dict_token_idf = idf(doc_tokens)
    for label, doc_tokenized in doc_tokens:
        dict_doc_token_tfidf = dict()
        for token in doc_tokenized:
            term_freq = tf(token, doc_tokenized)
            dict_doc_token_tfidf[token] = term_freq * dict_token_idf[token]
        doc_features.append((dict_doc_token_tfidf, label))

    return doc_features


def extract_high_features(doc_features, num_features=-1):
    lbl_features = list()
    for features, label in doc_features:
        dict_features = OrderedDict()
        for key, value in sorted(features.items(), key=lambda d: d[1], reverse=True)[:num_features]:
            dict_features[key] = value
        lbl_features.append((dict_features, label))
    return lbl_features


if __name__ == '__main__':
    dirs = r'D:\校园\信息131\大三下\计算机检索\实验3\code\19113124'
    list_files = traverse_dir(dirs)
    doc_tokens = prepare_labeled_tokens(list_files)
    doc_features = tfidf(doc_tokens)
    features_tfidf = extract_high_features(doc_features, 100)
    for d_features, doc in features_tfidf:
        print(doc)
        for token, idf in d_features.items():
            print('      ', token, idf)
        
