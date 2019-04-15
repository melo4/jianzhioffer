# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 下午7:34
# @Author  : Meng Xiao
class Solution:
    def getTranslationCount(self, num):
        if not isinstance(num, int) or num < 0:
            return
        str_num= str(num)
        length = len(str_num)
        counts = [0] * length     # 表示从第i位开始的不同翻译的数目

        for i in range(length-1, -1, -1):
            if i == length - 1:
                counts[i] = 1
                continue

            count = counts[i+1]
            value = (ord(str_num[i]) - ord('0')) * 10 + (ord(str_num[i+1]) - ord('0'))
            if i == length - 2:
                count += 1 if 10 <= value <= 25 else 0
            else:
                count += counts[i+2] if 10 <= value <= 25 else 0
            counts[i] = count
        return counts[0]

s = Solution()
print(s.getTranslationCount(12258))

