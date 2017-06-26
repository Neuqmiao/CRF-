#! python3
# -*- coding: utf-8 -*-
import os
from openpyxl import Workbook
import collections
"""计算召回率，准确率，F值
根据机器学习的输出结果output.txt来计算:
比方说输出结果是这样
第一列  第二列  第三列
  各     B      B
  级     C      C
  领     C      C
  导     C      C
  干     C      C
  部     E      E
  要     B      B
  把     E      E
  学     B      B
  习     E      E
  党     B      B
  章     E      E
  作     N      N
  为     N      N
  必     B      B
  须     C      C
  课     E      E
                  第三列正确B的个数(也就是跟第二列和第三列所在行都为B的个数)
第一种算法：召回率=———————————————————         
                  第二列所有B的个数
           
                  第三列正确B的个数
           准确率=——————————————————
                  第三列所有B的个数
                                   (α^2 + 1) * P * R       2 * P * R
           F值(也称加权调和平均数)=  ———————————————————  =  ————————————  (当α=1时，也就是F1)
                                   α^2 * (P + R)             P + R
                                         
要注意：这种计算方式要计算B, C, E, N, BE五种召回率
十份数据算平均F值得到最终的目标F值。如果大于95%(也就是概率论中的置信区间，显著性水平),就说明成功了，否则就要改变分词策略重新分词，
如果成功，取十份F值最大的model,将大量原始文本用(。!;?)分句完，让机器直接根据model去学习，crf_test -m model raw.txt > output.txt
然后根据生成的标签文本进行逆向处理，将文本还原成斜杠分割的样子

第二种算法: 第一列      第二列       第三列
                        B           B
                        C           E
                        E           B
                        B           C
                        E           E
                        B           B
                        E           E      
以B开头E结尾的是一个词，在这样的规则下，左右两边只有第三个词是完全对上的

       第三列正确的词只有一个      1
准确率=——————————————————————= ————
        第三列总共有三个词        3         
        
        第三列正确的词只有一个     1
召回率=——————————————————————= ————
        第二列所有的词有三个       3   
F值计算方法一样
"""


def ergodic():
    directory_paths = []
    for root, dirs, files in os.walk(r'D:\TenTest'):
        for directory in dirs:
            if directory.isdigit() and directory != ".idea":
                print(r'%s\%s' % (root, directory))
                directory_path = r'%s\%s' % (root, directory)
                directory_paths.append(directory_path)
    return directory_paths


def read_output(directory_path):
    with open(r'%s\%s' % (directory_path, "output.txt"), 'r') as f:
        data = f.read()
        return data


def census(data):
    row = data.split('\n')  # 先按行分割
    regular_list = list(map(str.split, filter(lambda x: len(x) > 0, row)))  # 去掉字符串为空的
    B_third_col_count = len(list(filter(lambda x: x == 'B', [x[-1] for x in regular_list]))) # 第三列所有B的个数
    C_third_col_count = len(list(filter(lambda x: x == 'C', [x[-1] for x in regular_list])))
    E_third_col_count = len(list(filter(lambda x: x == 'E', [x[-1] for x in regular_list])))
    N_third_col_count = len(list(filter(lambda x: x == 'N', [x[-1] for x in regular_list])))

    B_second_col_count = len(list(filter(lambda x: x == 'B', [x[-2] for x in regular_list]))) # 第二列所有B的个数
    C_second_col_count = len(list(filter(lambda x: x == 'C', [x[-2] for x in regular_list])))
    E_second_col_count = len(list(filter(lambda x: x == 'E', [x[-2] for x in regular_list])))
    N_second_col_count = len(list(filter(lambda x: x == 'N', [x[-2] for x in regular_list])))

    B_right_third_col_count = len(list(filter(lambda item: item[0] == item[1] == 'B', [x[1:] for x in regular_list])))
    C_right_third_col_count = len(list(filter(lambda item: item[0] == item[1] == 'C', [x[1:] for x in regular_list])))
    E_right_third_col_count = len(list(filter(lambda item: item[0] == item[1] == 'E', [x[1:] for x in regular_list])))
    N_right_third_col_count = len(list(filter(lambda item: item[0] == item[1] == 'N', [x[1:] for x in regular_list])))

    parameter = [B_third_col_count, C_third_col_count, E_third_col_count, N_third_col_count,
                 B_second_col_count,C_second_col_count, E_second_col_count, N_second_col_count,
                 B_right_third_col_count,C_right_third_col_count, E_right_third_col_count, N_right_third_col_count]
    # 0 1 2 3
    # 4 5 6 7
    # 8 9 10 11
    return parameter


def formulate(param):
    B_recall_rate = param[8] / param[4]
    print(B_recall_rate)
    C_recall_rate = param[9] / param[5]
    print(C_recall_rate)
    E_recall_rate = param[10] / param[6]
    print(E_recall_rate)
    N_recall_rate = param[11] / param[7]
    print(N_recall_rate)

    B_accuracy_rate = param[8] / param[0]
    print(B_accuracy_rate)
    C_accuracy_rate = param[9] / param[1]
    print(C_accuracy_rate)
    E_accuracy_rate = param[10] / param[2]
    print(E_accuracy_rate)
    N_accuracy_rate = param[11] / param[3]
    print(N_accuracy_rate)

    B_F_value = (2 * B_recall_rate * B_accuracy_rate) / (B_recall_rate + B_accuracy_rate)
    C_F_value = (2 * C_recall_rate * C_accuracy_rate) / (C_recall_rate + C_accuracy_rate)
    E_F_value = (2 * E_recall_rate * E_accuracy_rate) / (E_recall_rate + E_accuracy_rate)
    N_F_value = (2 * N_recall_rate * N_accuracy_rate) / (N_recall_rate + N_accuracy_rate)
    average_F_value = (B_F_value + C_F_value + E_F_value + N_F_value) / 4

    result = collections.OrderedDict([('B_recall_rate', B_recall_rate), ('C_recall_rate', C_recall_rate), ('E_recall_rate', E_recall_rate), ('N_recall_rate', N_recall_rate),
                                      ('B_precision_rate', B_accuracy_rate), ('C_precision_rate', C_accuracy_rate), ('E_precision_rate', E_accuracy_rate), ('N_precision_rate', N_accuracy_rate),
                                      ('B_F_value', B_F_value), ('C_F_value', C_F_value), ('E_F_value', E_F_value), ('N_F_value', N_F_value), ('average_F_value', average_F_value)])
    return result


def save_data_to_excel(save_path, param):
    book = Workbook()
    sheet = book.active

    for key, value in enumerate(param.items()):
        sheet['%s%s' % ('A', key+1)] = value[0]
        sheet['%s%s' % ('B', key+1)] = value[1]
    book.save(r'%s\data.xlsx' % save_path)


if __name__ == '__main__':
    dir_paths = ergodic()
    print(dir_paths)
    for dp in dir_paths:
        content = read_output(dp)
        data_collection = census(content)
        probability_collection = formulate(data_collection)
        save_data_to_excel(dp, probability_collection)

    # content = read_output('cal.txt')
    # data_collection = census(content)
    # print(data_collection)
    # probability_collection = formulate(data_collection)
    # print(probability_collection)
    # save_data_to_excel(probability_collection)

    # test = {'a': 1, 'b': 1}
    # for key, value in enumerate(test.items()):
    #     print(key)
    #     print(value[-1])

    # res = read_output('cal.txt')
    # test = res.split('\n')
    # print(test)
    # non_none = list(map(str.split, filter(lambda x: len(x) > 0, test)))
    # print(non_none)

    # non_none = [x for x in test if len(x) != 0]
    # sub = list(map(str.split, non_none))
    # print(sub)

    # regular_list = [['a', 'b', 'b'], ['d', 'e', 'e']]
    # print(list(filter(lambda x: x == 'b', [x[-2] for x in regular_list])))
    # print(list(filter(lambda item: item[0] == item[1] == 'e', [x[1:] for x in regular_list])))
    # print([x[1:] for x in regular_list])
