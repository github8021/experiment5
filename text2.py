# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment5
# @File     :text2
# @Date     :2020/9/28 18:49
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
d = {"联想(Lenovo)小新Pro13高性能轻薄本 ": 5299,
     "联想(Lenovo)小新Air14性能版轻薄本": 4999,
     "联想(Lenovo)小新15 2020性能版轻薄本": 5199,
     "荣耀笔记本电脑MagicBook": 3499,
     "华为笔记本电脑 MateBook": 4899,
     "宏碁(Acer)暗影骑士·擎": 5899,
     "戴尔DELL灵越5000": 4199,
     "华硕(ASUS) VivoBook15s": 4499,
     "惠普（HP）战66": 4599,
     "Apple MacBook Air 13.3": 5499}
print(sorted(d.items(), key=lambda item: item[1], reverse=True))
