# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 下午5:24
# @Author  : Meng Xiao
class Solution:
    def is_Prime(self, n):
        for i in range(2,int(n ** 0.5)+1):
            flag = n % i
            if flag == 0:
                return False
        return True
    def prime_de(self, n):
        if self.is_Prime(n):
            return [n]
        prime = []
        for i in range(2, n//2):
            if self.is_Prime(i):
                prime.append(i)
        print(prime)
        for item in prime:
            while n % item == 0:
                print(item)
                n /= item
            continue
        return


s = Solution()
print(s.prime_de(45))