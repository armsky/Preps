"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return 2147483647

Have you met this question in a real interview?
Example
Given dividend = 100 and divisor = 9, return 11.
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX = 2147483647
        if divisor == 0:
            return MAX
        neg = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        res = self.helper(abs(dividend), abs(divisor))
        if neg:
            return max(-MAX - 1, -res)
        else:
            return min(MAX, res)

    def helper(self, dividend, divisor):
        if dividend < divisor:
            return 0
        sum = divisor
        divide = 1
        while (sum + sum) <= dividend:
            sum += sum
            divide += divide
            print sum, divide, dividend - sum, divisor
        return divide + self.helper(dividend - sum, divisor)
