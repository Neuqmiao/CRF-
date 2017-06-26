#! python3
# -*- coding: utf-8 -*-
import glob

# print(glob.glob("./*.txt"))

files_list = glob.glob("./*.txt")
for file in files_list:
    # print(file.replace('.\\', ''))
    with open('%s' % file.replace('.\\', ''), 'r') as f:
        data = f.read()
        split_by_n = [x for x in data.split('\n') if x != '']
        print(split_by_n)
        res = []
        for word in split_by_n:
            if word.endswith('B'):
                start_word = '/' + word.replace('\tB', '')
                res.append(start_word)
            elif word.endswith('C'):
                middle_word = '/' + word.replace('\tC', '')
                res.append(middle_word)
            elif word.endswith('E'):
                end_word = word.replace('\tE', '') + '/'
                res.append(end_word)
            elif word.endswith('N'):
                n_word = word.replace('\tN', '')
                res.append(n_word)
        save_format = ''.join(res).replace('//', '/')
    with open('restore/restore_%s' % file.replace('.\\', ''), 'w') as f:
        f.write(save_format)
        # print(save_format)
        # print(split_by_n)
    # with open('', 'w') as f:

    # break

