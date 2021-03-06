"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    # DFS version
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, a, i, tmp):
        if i == len(a):
            self.res.append(tmp)
            return
        self.dfs(a, i+1, tmp+[a[i]])
        self.dfs(a, i+1, tmp)

    # Iterative version
    def subsets(self, S):
        R = [[]]
        for s in sorted(S):
            R += [r+[s] for r in R]
        return R
