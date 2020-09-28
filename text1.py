# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment5
# @File     :text1
# @Date     :2020/9/28 18:18
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import random

a = ['谢谢惠顾', '谢谢惠顾', '谢谢惠顾', '谢谢惠顾', '谢谢惠顾', '一等奖', '二等奖', '三等奖']
print(f"本次抽奖有：{a}")
input("请刮去位置(1-8)：")
b = random.randint(1, 8)-1
print(a.__getitem__(b))
