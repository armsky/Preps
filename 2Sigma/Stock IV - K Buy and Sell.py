"""
Say you have an array for which the ith element is the price of a given stock on
day i.

Design an algorithm to find the maximum profit. You may complete at most k
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell
the stock before you buy again).
"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k >= n/2:
            return self.quickSolve(prices, n)
        # t[i][j]: max profix for up to i transactions by time j
        # (0<=i<=k, 0<=j<=T)
        t = [[0 for _ in range(n)] for _ in range(k+1)]
        for i in range(1, k+1):
            tmpMax = -prices[0]
            for j in range(1, n):
                t[i][j] = max(t[i][j-1], tmpMax + prices[j])
                tmpMax = max(tmpMax, t[i-1][j-1] - prices[j])
        return t[k][n-1]

    def quickSolve(self, prices, n):
        pro = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                pro += prices[i] - prices[i-1]
        return pro
