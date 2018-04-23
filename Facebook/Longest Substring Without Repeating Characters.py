"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        map = {}
        res = 0
        j = 0
        for i in range(len(s)):
            c = s[i]
            if c in map:
                res = max(res, i - j)
                j = max(j, map[c] + 1)
            map[c] = i
        return max(res, len(s) - j) #Need to get last update here.
