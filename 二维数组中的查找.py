# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 下午4:11
# @Author  : Meng Xiao
def findE(list2d, x):
    if list2d == []:
        return False
    m = len(list2d)
    n = len(list2d[1])
    i = 0
    j = n-1
    while i < m and j >=0:
        if x == list2d[i][j]:
            return True
        if x < list2d[i][j]:
            j -= 1
        else:
            i += 1
    return False
list2d = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(findE(list2d,5))