# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment5
# @File     :text3
# @Date     :2020/9/28 18:59
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import random

k = 4
matrix = [[0 for i in range(3)] for i in range(3)]
flag = True
while (k > 0):
    for i in range(3):
        for j in range(3):
            b = random.randint(-4, 3)
            if (b >= 0 and matrix[i][j] != 1):
                matrix[i][j] = 1
                k -= 1
                if (k == 0):
                    flag = False
                    break
            else:
                matrix[i][j] = 0
        if not flag:
            break
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end="\t")
    print()
