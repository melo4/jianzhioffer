# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 下午8:49
# @Author  : Meng Xiao
class Solution:
    def isNumeric(self, s):
        if len(s) <= 0:
            return False
        # 分别标记是否出现过正负号、小数点、e
        has_sign  = False
        has_point = False
        has_e = False
        for i in range(len(s)):
            if s[i] == 'E' or s[i] == 'e':
                #不同时出现两个e
                if has_e:
                    return False
                else:
                    has_e = True
                    if i == len(s) - 1:  # e不能出现在最后
                        return False
            elif s[i] == '+' or s[i] == '-':
                if has_sign:
                    if s[i-1] != 'e' and s[i-1] != 'E':
                        return False
                # 如果这是第一次出现符号位，而且出现的位置不是字符串第一个位置，那么就只能出现在e后面
                else:
                    has_sign = True
                    if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                        return False

            elif s[i] == '.':
                # 小数点不能出现两次并且如果出现过e，则不能再出现小数点
                if has_point or has_e:
                    return False
                else:
                    has_point = True
                    if i > 0 and has_e:
                        return False
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
        return True


