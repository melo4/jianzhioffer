# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 下午9:18
# @Author  : Meng Xiao

def josephus(n, m):
    """
     环的问题，
     共有n个人围成一圈，从1开始报数，数到m时退出，再从1开始，直到所有人退出
    """
    people = list(range(1, n+1))
    index = 0
    # 给n个人编号放到people列表中，1号的下标为0
    for i in range(n):
        count = 0
        while count < m:
            if people[index] != 0:
                count += 1
            if count == m:
                print(people[index],'out!')
                #把退出的人编号置0
                people[index] = 0
            index = (index + 1) % n
    return



# 递推公式法 f(n,m) = (f(n-1,m) + m) % n
def josephus1(n, m):
    index = 1
    for i in range(2, n+1):
        index = (index+m) % i
    return index

print(josephus1(10,6))