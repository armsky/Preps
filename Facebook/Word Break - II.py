"""
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is a
valid dictionary word. You may assume the dictionary does not contain duplicate
words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
class Solution(object):

    #NOTE: With cache (From Leetcode)
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.dfs(0, len(s), s, wordDict, {})

    def dfs(self, start, end, s, wordDict, cache):
        if start in cache:
            return cache[start]
        current = start
        cache[start] = []
        candidate= ''
        while current < end:
            candidate += s[current]
            current += 1
            if candidate in wordDict:
                if current == end:
                    cache[start].append(candidate)
                else:
                    for word in self.dfs(current, end, s, wordDict, cache):
                        cache[start].append(candidate + ' ' + word)
        return cache[start]

    # NOTE: NAIVE GOT TLE
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        if not wordDict and not s:
            return True
        map = {}
        for word in wordDict:
            map[word] = 1
        self.res = []
        self.dfs(s, map, '')
        return self.res

    def dfs(self, s, map, temp):
        if not s:
            self.res.append(temp.strip())
        for i in range(len(s)):
            if s[:i+1] in map:
                self.dfs(s[i+1:], map, temp+' '+s[:i+1])
