#! python3
# -*- coding: utf-8 -*-


# class getoutofloop(Exception):
#     pass
#
#
# try:
#     for i in range(5):
#         for j in range(5):
#             for k in range(5):
#                 if i == j == k == 3:
#                     raise getoutofloop()
#                 else:
#                     print(i, '----', j, '----', k)
# except getoutofloop:
#     pass


# for i in range(5):
#     for j in range(5):
#         for k in range(5):
#             if i == j == k == 3:
#                 break
#             else:
#                 print(i, '----', j, '----', k)
#         else:
#             continue
#         break
    # else:
    #     continue
    # break


# def test():
#     for i in range(5):
#         for j in range(5):
#             for k in range(5):
#                 if i == j == k == 3:
#                     return
#                 else:
#                     print(i, '----', j, '----', k)
# test()