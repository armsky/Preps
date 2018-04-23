"""
Given a string containing only digits, restore it by returning all possible
valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.dfs(s, 0, [], 0)
        return self.res

    def dfs(self, s, i, tmp, cnt):
        if cnt >= 4 or i >= len(s):
            if cnt == 4 and i == len(s):
                self.res.append('.'.join(tmp))
            return
        if s[i] == '0':
            self.dfs(s, i+1, tmp+[s[i]], cnt+1)
        else:
            for k in range(1,4):
                j = i+k
                r = s[i:j]
                if j <= len(s) and int(r) <= 255:
                    self.dfs(s, j, tmp+[r], cnt+1)
