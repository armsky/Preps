"""
The count-and-say sequence is the sequence of integers with the first five terms
as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(2, n+1):
            s = self.count(s)
        return s

    def count(self, s):
        cnt = 0
        cur = '#'
        t = ''
        for i in range(len(s)):
            if s[i] != cur:
                if cur != '#':
                    t += str(cnt) + cur
                cur = s[i]
                cnt = 1

            else:
                cnt += 1
        t += str(cnt) + cur
        return t
