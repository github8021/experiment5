# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment5
# @File     :text3_2
# @Date     :2020/9/28 19:33
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import random

matrix = [[0 for i in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        matrix[i][j] = random.randint(108, 111)

for i in range(3):
    for j in range(3):
        print(matrix[i][j], end="\t")
    print()
