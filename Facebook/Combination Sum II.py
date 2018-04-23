"""
Given a collection of candidate numbers (C) and a target number (T), find all
unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(candidates, 0, 0, target, [])
        return self.res

    def dfs(self, a, i, sum, target, tmp):
        if sum == target:
            tmp.sort()
            if tmp not in self.res:
                self.res.append(tmp)
            return
        if i < len(a):
            if a[i] + sum <= target:
                self.dfs(a, i+1, sum+a[i], target, tmp+[a[i]])
            self.dfs(a, i+1, sum, target, tmp)
