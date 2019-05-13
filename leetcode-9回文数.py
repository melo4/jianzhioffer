# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 20:00
# @Author  : Meng Xiao

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        rev, y = 0, x
        while x > 0:
            rev = rev * 10 + x % 10
            x /= 10
        return y == rev