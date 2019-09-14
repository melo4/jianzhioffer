# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 16:36
# @Author  : Meng Xiao
'''
算法原理
(1) 初始随机选取k个中心点；
(2) 遍历每个样本，选取距离每个样本最近的中心点，归为该类；
(3) 更新中心点为每类的均值；
(4) 重复(2)(3)迭代更新，直至误差小到某个值或者到达一定的迭代步数.
'''
import numpy as np
import math
def kmeans(k):
    m, n = 100, 20 # 构造样本， 100行， 20列
    x = 10 * np.random.random((m, n))
    # 随机选取k个初始中心点
    init_cent_sample = set()
    while len(init_cent_sample) < k:
        init_cent_sample.add(np.random.randint(0, m))
    cent = x[list(init_cent_sample)]

    # 记录每个样本的类归属
    cluster_assessment = np.zeros((m, 2))  # [类， 距离]

    # 记录每个类的中心点在本次迭代后是否有过改变
    cent_changed = True
    while cent_changed:
        cent_changed = False

        for j in range(m):
            min_idx = -1  # 记录每个样本距离最近的类
            min_dist = math.inf  # 记录每个样本的最小类距离

            for i in range(k):
                d = distance(x[j], cent[i])
                if d < min_dist:
                    min_dist = d
                    min_idx = i

            # 记录是否发生变化
            if min_idx != cluster_assessment[j][0]:
                cluster_assessment[j] = np.array([min_idx, min_dist])
                cent_changed = True
        print(cluster_assessment)

        # 更新每个类的中心点：均值
        for i in range(k):
            cent_i_samples = np.where(cluster_assessment[:, 0] == i)
            if len(cent_i_samples) > 0:
                print(cent_i_samples)
                cent[i] = np.mean(x[cent_i_samples], axis=0)


def distance(a, b):
    return math.sqrt(sum(pow(a-b, 2)))

kmeans(10)

