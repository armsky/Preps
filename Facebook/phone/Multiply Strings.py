"""
Given two non-negative integers num1 and num2 represented as strings, return the
product of num1 and num2

Have you met this question in a real interview?
Example
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer
directly.
"""
class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    def multiply(self, num1, num2):
        if not num1 or not num2:
            return None
        if num1 =='0' or num2 == '0':
            return '0'

        m1, m2 = len(num1), len(num2)
        ans = []
        for i, n1 in enumerate(num1[::-1]):
            for j, n2 in enumerate(num2[::-1]):
                pro = int(n1) * int(n2)
                if i+j >= len(ans):
                    ans.append(pro)
                else:
                    ans[i+j] += pro
        carry = 0
        for i, n in enumerate(ans):
            val = n + carry
            ans[i] = val % 10
            carry = val / 10
        while carry:
            ans.append(carry % 10)
            carry /= 10
        print ans
        return ''.join(map(str, ans[::-1]))
