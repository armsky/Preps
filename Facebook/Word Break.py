"""
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated sequence
of one or more dictionary words. You may assume the dictionary does not contain
duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code"
"""
class Solution(object):
    # A DP solution that passed
    def wordBreak(self, s, dict):
        if not dict:
            return not s
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        # Good way to reduce time
        max_word_len = max([len(w) for w in dict])
        for i in range(1, n+1):
            for j in range(1, min(i, max_word_len) + 1):
                if dp[i-j] == True and s[i-j:i] in dict:
                    dp[i] = True
                    break
                print dp, i, j
        return dp[len(s)]

    # NOTE: Second try, record the longest word in dict, still TLE
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict and not s:
            return True
        map = {}
        maxlen = 0
        for word in wordDict:
            map[word] = 1
            maxlen = max(maxlen, len(word))
        self.res = False
        self.dfs(s, map, maxlen)
        return self.res

    def dfs(self, s, map, maxlen):
        if not s:
            self.res = True
            return
        for i in range(1, min(maxlen, len(s)) + 1):
            if s[:i] in map:
                self.dfs(s[i:], map, maxlen)

    #NOTE: A DFS solution, got TLE
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict and not s:
            return True
        map = {}
        for word in wordDict:
            map[word] = 1
        self.res = False
        self.dfs(s, map)
        return self.res

    def dfs(self, s, map):
        if not s:
            self.res = True
        for i in range(len(s)):
            if s[:i+1] in map:
                self.dfs(s[i+1:], map)
