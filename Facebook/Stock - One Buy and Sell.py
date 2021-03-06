"""
Say you have an array for which the ith element is the price of a given stock on
day i.

If you were only permitted to complete at most one transaction (ie, buy one and
sell one share of the stock), design an algorithm to find the maximum profit.

Have you met this question in a real interview?
Example
Given array [3,2,3,1,2], return 1.
"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices or len(prices)<2:
            return 0
        pre = [0]
        pro = 0
        for i in range(1, len(prices)):
            pre.append(max(0, prices[i] - prices[i-1] + pre[-1]))
            pro = max(pro, pre[-1])
        return pro
