"""
Given a collection of numbers that might contain duplicates, return all possible
unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        visited = [False for _ in range(len(nums))]
        res = []
        nums.sort()
        self.dfs(nums, res, [], visited)
        return res

    def dfs(self, nums, res, tmp, visited):
        if len(nums) == len(tmp):
            res.append(list(tmp))
            return
        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]): #Don't forget i > 0
                continue
            visited[i] = True
            tmp.append(nums[i])
            self.dfs(nums, res, tmp, visited)
            tmp.pop()
            visited[i] = False
