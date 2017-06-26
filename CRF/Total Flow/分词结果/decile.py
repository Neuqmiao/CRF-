#! python3
# -*- coding: utf-8 -*-
"""分成10份语料的算法"""
import os
import xlrd
import random
import subprocess


def chaos():  # 进行句子乱序排列
    total_string = ''
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.txt'):
            with open(filename, 'r') as f:
                data = f.read()
                total_string += data
    new_string = total_string.replace('\n', '').replace('。', '。$').replace('；', '；$').replace('！', '！$').replace('？', '？$')
    all_content = new_string.split('$')
    # print(all_content)
    # print(len(all_content))
    random.shuffle(all_content)
    # print(all_content)
    length = len(all_content)
    remainder = length % 10
    if remainder == 0:  # 将语料列表等分成10个长度相同的子列表并放在一个列表中
        average_upper = int(length / 10)
        ten_slice_list = [all_content[i:i+average_upper] for i in range(0, length, average_upper)]
        return ten_slice_list
        # for i in range(10):
        #     simulate_content = ten_slice_list[i]
        #     training_content = sum([x for x in ten_slice_list if x not in ten_slice_list[i]], [])

    else:  # 当不能被整除时,切分好的列表[[], [], []... []]
        average_upper = int((length - remainder) / 10)
        slice_list = [all_content[i:i + average_upper] for i in range(0, length, average_upper)]
        for index, value in enumerate(slice_list[-1]):
            slice_list[index].append(value)
        ten_slice_list = slice_list[:-1]
        # for i in range(10):
        #     simulate_content = ten_slice_list[i]
        #     training_content = sum([x for x in ten_slice_list if x not in ten_slice_list[i]], [])
        return ten_slice_list

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
    # training, simulate = chaos()
    # print(training)
    # print(simulate)
    # corpus = read_xlsx(r'words.xlsx')  # 词库
    # training_save_format = ''.join(make_label(training, corpus))
    # simulate_save_format = ''.join(make_label(simulate, corpus))
    # with open('training.txt', 'w') as f:
    #     f.write(training_save_format)
    # with open('simulate.txt', 'w') as f:
    #     f.write(simulate_save_format)
    # [1,2,3,4,5,6,7,8,9,10,11] -->[[1, 11],[2],[3],[4],[5],[6],[7],[8],[9],[10]]

    # upper = 1
    # all_content = [1,2,3,4,5,6,7,8,9,10,11]
    # ten_slice_list = [all_content[i:i + upper] for i in range(0, 11, upper)]
    # for index, value in enumerate(ten_slice_list[-1]):
    #     print(index, value)
    #     ten_slice_list[index].append(value)
    # print(ten_slice_list[:-1])

    # output = [map(sum(i, ten_slice_list[])) for i in ten_slice_list[-1]]
    # test = [i for k in ten_slice_list[-1] for i in k]  # k是sublist,i是sublist中的每个元素
    # print(ten_slice_list)
    # test = ['a', 'b', 'c']
    # print(''.join(test))
    # test = [['a', 'b'], ['c', 'd']]
    # print(sum(test, []))

    # corpus = read_xlsx(r'words.xlsx')
    # ten_average_list = chaos()
    # print(ten_average_list)
    # print(len(ten_average_list))
    # for i in range(0, len(ten_average_list)):
    #     simulate_content = ten_average_list[i]
    #     training_content = sum([x for x in ten_average_list if x != ten_average_list[i]], [])
    #     print(ten_average_list[i])

    # corpus = read_xlsx(r'words.xlsx')
    # ten_average_list = chaos()
    # for i in range(0, 10):
    #     simulate_content = ten_average_list[i]
    #     print(simulate_content)
    #     training_content = sum([x for x in ten_average_list if x != ten_average_list[i]], [])
    #     print(training_content)
    #     training_res = ''.join(make_label(training_content, corpus))
    #     simulate_res = ''.join(make_label(simulate_content, corpus))
    #     if not os.path.exists(r'.\%s' % i):
    #         os.makedirs(r'.\%s' % i)
    #         with open('%s/test.txt' % i, 'w') as f:
    #             f.write(simulate_res)
    #         with open('%s/training.txt' % i, 'w') as f:
    #             f.write(training_res)

    rootpath = r'D:\Python35 Project\CRF\Total Flow\分词结果'

    for subdir, dirs, files in os.walk(rootpath):
        for dirc in dirs:
            path = r'%s\%s\training.txt' % (rootpath, dirc)
            model_path = r'%s\%s\model' % (rootpath, dirc)
            print(path)
            print(model_path)
            print("crf_learn template %s %s" % (path, model_path))
            # subprocess.call("crf_learn template %s %s" % (path, model_path))
            break

    # for i in range(0, 10):
    #     subprocess.call("crf_learn template D:\Python35 Project\CRF\Total Flow\分词结果\\0\\training.txt model")
    #     subprocess.call("cd ..")

    # ten_average_list = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    # for i in range(0, 10):
    #     simulate_content = ten_average_list[i]
    #     training_content = sum([x for x in ten_average_list if x != ten_average_list[i]], [])
    #     print(simulate_content)
    #     print(training_content)

