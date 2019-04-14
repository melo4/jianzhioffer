# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 下午9:14
# @Author  : Meng Xiao
'''
http://www.cnblogs.com/qiaojushuang/p/7780445.html
'''
class Solution:
    def get_digits(self, n):
        # 求整数n的位数
        ret = 0
        while n:
            ret += 1
            n //= 10
        return ret

    def get1digits(self, n):
        # 获取每个位数之间1的总数，n位位数，n=2即10-99
        if n < 0:
            return 0
        if n == 1:
            return 1
        current = 9 * self.get1digits(n-1) + 10 ** (n-1)
        return self.get1digits(n-1) + current

    def get1nums(self, n):
        if n < 10:
            return 1 if n >= 1 else 0
        digit = self.get_digits(n) # 获得位数
        low_nums = self.get1digits(digit-1) #最高位之前的1的个数
        high = int(str(n)[0]) #最高位
        low = n - high * 10 ** (digit-1) # 低位

        if high == 1:
            high_nums = low + 1
            all_nums = high_nums
        else:
            high_nums = 10 ** (digit-1)
            all_nums = high_nums + low_nums * (high-1)
        return low_nums + all_nums + self.get1nums(low)





s = Solution()
print(s.get1nums(12))