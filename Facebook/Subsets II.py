"""
Given a collection of integers that might contain duplicates, nums, return all
possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        self.res = []
        nums.sort()
        v = [False for _ in range(n)]
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, a, i, tmp):
        if i == len(a):
            self.res.append(tmp)
            return

        self.dfs(a, i+1, tmp+[a[i]])
        self.dfs(a, i+1, tmp)
