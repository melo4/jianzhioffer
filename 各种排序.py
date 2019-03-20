# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 下午3:04
# @Author  : Meng Xiao

# 1.
def insert_sort(lists):
    '''
    直接插入排序：
    从第一个元素开始，作为已排序元素，对于未排序数据，在已排序列中
    从后往前扫描，找到相应位置插入。
    O(n2) O(1) 稳定
    '''
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

def shell_sort(lists):
    '''
    希尔排序：
    将整个待排序的序列分割为若干子序列分别进行直接插入排序
    O(n1.3) O(1)
    '''
    count = len(lists)
    step = 2
    group = count // step # 初始增量为数组长度的一半
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group //= step
    return lists

def select_sort(lists):
    '''
    ˙直接选择排序：
    多趟选择，每次选择最小（大）元素放在已排末尾。
    O(n2) O(1)
    '''
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j              #寻找最小的数，将最小的数索引保存
        lists[min], lists[i] = lists[i], lists[min]
    return lists




# 堆排序，建堆，堆调整，排序
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size // 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

def build_heap(lists, size):
    for i in range(0, (size//2))[::-1]:
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists

def bubble_sort(lists):
    '''
    两两交换 可用于内存足够的TopK
    O(n2), O(1)
    '''
    count = len(lists)
    for i in range(0,count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


def quick_sort(lists, left, right):
    '''
    通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，
    则可分别对这两部分记录继续进行排序，以达到整个序列有序。
    O(nlogn) O(nlogn)
    '''
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left-1)
    quick_sort(lists, left+1, high)
    return lists
