# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 下午9:45
# @Author  : Meng Xiao
class Solution:
    # 只允许交易一次
    def maxDiff1(self, numbers):
        if not numbers or len(numbers) < 2:
            return 0
        minD = numbers[0] # 保存前i-1个数字的最小值
        maxDiff = numbers[1] - minD
        for i in range(2, len(numbers)):
            if numbers[i-1] < minD:
                minD = numbers[i-1]
            curDiff = numbers[i] - minD
            if curDiff > maxDiff:
                maxDiff = curDiff
        return maxDiff

    # 允许无数次交易
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        maxprof = 0
        minprice = 2 ** 32
        for p in prices:
            # 如果今天价格小于昨日价格，只更新minprice
            if p <= minprice:
                minprice = p
            # 今天价格大于昨日价格，最终受益加上这一段，并更新
            else:
                maxprof += (p-minprice)
                minprice = p
        return maxprof

    # 允许2次交易\
    '''
    动态规划法。以第i天为分界线，计算第i天之前进行一次交易的最大收益preProfit[i]，
    和第i天之后进行一次交易的最大收益postProfit[i]，
    最后遍历一遍，max{preProfit[i] + postProfit[i]} (0≤i≤n-1)就是最大收益。
    第i天之前和第i天之后进行一次的最大收益求法同1。
    '''
    def maxProfit2(self, prices):
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        preProfit = [0] * n
        postProfit = [0] * n

        curMin = prices[0]
        for i in range(1, n):
            curMin = min(curMin, prices[i])
            preProfit[i] = max(preProfit[i-1], prices[i]-curMin) # 第i天卖出

        curMax = prices[n-1]
        for i in range(n-2, -1, -1):
            curMax = max(curMax, prices[i])
            postProfit[i] = max(postProfit[i+1], curMax-prices[i]) # 第i天买入

        maxProfit = 0
        for i in range(n):
            maxProfit = max(maxProfit, preProfit[i]+postProfit[i])

        return maxProfit

    # 允许K次交易
    # https://blog.csdn.net/Dr_Unknown/article/details/51939121
    def maxProfit_k(self, k, prices):
        if len(prices) < 2:
            return 0
        if k > len(prices):
            return self.maxProfit(prices)
        local = [[0 for i in range(k+1)] for j in range(len(prices))]
        globa = [[0 for i in range(k + 1)] for j in range(len(prices))]
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            for j in range(1, k+1):
                local[i][j] = max(globa[i-1][j-1]+max(0,diff), local[i-1][j]+diff)
                globa[i][j] = max(local[i][j], globa[i-1][j])
        return globa[len(prices)-1][k]

