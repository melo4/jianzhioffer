# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 下午3:39
# @Author  : Meng Xiao

a = [1,2,2,2,5,7,8,8]
a.sort()
maxn = a[-1] #最大数
minn = a[0] #最小数
dict = {} # 数字对应出现的次数
for x in range(minn,2*maxn):
    dict[x] = 0
for ii in a:
    dict[ii] += 1
count = 0 # 记录操作次数
for key in dict:
    if dict[key] > 1:
        for i in range(dict[key]-1):
            for nn in dict:
                if nn > key and dict[nn] == 0:
                    dict[nn] += 1
                    count += (nn - key)
                    break
print(count)
