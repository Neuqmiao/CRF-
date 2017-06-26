#! python3
# -*- coding: utf-8 -*-


def make_label(filename):
    with open(filename, 'r') as f:
        content = f.read()
    origin_list = content.split('/')
    print(origin_list)
    pure_list = [x for x in origin_list if x != '\n' and x != ' ' and x != '']
    print(pure_list)

if __name__ == '__main__':
    make_label('slash_test.txt')
