# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 下午4:22
# @Author  : Meng Xiao
class Solution:
    def PrintNumber(self, number):
        isBeginning0 = True
        nLength = len(number)

        for i in range(nLength):
            if isBeginning0 and number[i] != '0':
                isBeginning0 = False
            if not isBeginning0:
                print('%c' %number[i], end='')
        print('')

    def Print1ToMaxOfNDigits(self, n):
        if n <= 0:
            return
        number = ['0'] * n
        for i in range(10):
            number[0] = str(i)
            self.Print1ToMaxOfNDigitsRecursively(number, n, 0)

    def Print1ToMaxOfNDigitsRecursively(self, number, length, index):
        if index == length - 1:
            self.PrintNumber(number)
            return
        for i in range(10):
            number[index+1] = str(i)
            self.Print1ToMaxOfNDigitsRecursively(number, length, index+1)

