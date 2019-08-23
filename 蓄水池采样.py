# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 19:43
# @Author  : Meng Xiao
import random
class ReservoirSample:
    def __init__(self, size):
        self._size = size
        self._counter = 0
        self._sample = []

    def feed(self, item):
        self._counter += 1
        # i <= k
        if len(self._sample) < self._size:
            self._sample.append(item)
            return self._sample
        # i > k
        rand_int = random.randint(1, self._counter)
        if rand_int <= self._size:
            self._sample[rand_int-1] = item
        return self._sample


from collections import Counter

def test_():
    samples = []
    for i in range(10000):
        rs = ReservoirSample(3)
        for item in range(1, 11):
            sample = rs.feed(item)
        samples.extend(sample)
    r = Counter(samples)
    print(r)
test_()