# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 14:43
# @Author  : Meng Xiao
'''
得到结果数据，数据结构为：输出概率（pctr），标签真值（click）
对结果数据按输出概率（pctr）进行从大到小排序
从大到小，把每一个输出概率作为分类阈值，统计该分类阈值下的TPR和FPR
微元法计算ROC曲线面积、绘制ROC曲线
'''
from matplotlib import pyplot as plt
def get_roc(data, pos, neg):
    data.sort(key=lambda x: x[0], reverse=True)
    roc_arr = []
    tp = fp = 0
    for sample in data:
        tp += (1 if sample[1] == 1 else 0)
        fp += (1 if sample[1] == -1 else 0)
        roc_arr.append((fp/neg, tp/pos))
    return roc_arr

def draw_roc(roc_arr):
    x = [sample[0] for sample in roc_arr]
    y = [sample[1] for sample in roc_arr]
    plt.title('ROC_curve')
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.plot(x, y)
    plt.show()

def get_auc(roc_arr):
    # 用微元法计算曲线下面积
    auc = 0.
    prev_x = 0
    for x, y in roc_arr:
        auc += (x-prev_x) * y
        prev_x = x
    return auc