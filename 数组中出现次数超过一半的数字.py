# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 下午2:29
# @Author  : Meng Xiao


class Solution:
    def MoreThanHalfNum(self, numbers):
        length = len(numbers)
        if not numbers:
            return 0
        result = numbers[0]
        times = 1

        for i in range(1, length):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        if not self.CheckMoreThanHalf(numbers, length, result):
            return False
        return result

    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1
        if times * 2 <= length:
            return False
        return True
