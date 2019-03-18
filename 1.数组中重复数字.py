# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 下午3:33
# @Author  : Meng Xiao
# @File    : 1.数组中重复数字.py
# @Software: PyCharm
def swap(i, j, a):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return a
def repeat_1(list):
    for i in range(len(list)):
        if list[i] != i:
            if list[i] == list[list[i]]:
                return list[i], True
            else:
                swap(list[i], list[list[i]], list)
        else:
            continue

    return False
# 以上为第一种方法

# 方法2 用哈希
def repeat_2(list):
    dict1 = dict()
    for i in list:
        if i not in dict1:
            dict1[i] = 1
        else:
            return i, True
    return False

if __name__ == '__main__':
    a = list(map(int, input('请依次输入数组元素\n').split()))
    #print(repeat_1(a))
    print(repeat_2(a))