"""
Given an array of n integers nums and a target, find the number of index
triplets i, j, k with 0 <= i < j < k < n that satisfy the condition
nums[i] + nums[j] + nums[k] < target.

Have you met this question in a real interview?
Example
Given nums = [-2,0,1,3], target = 2, return 2.

Explanation:
Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]
"""
class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    # O(n^2) solution 
    def threeSumSmaller(self, nums, target):
        n = len(nums)
        if not nums or n < 3:
            return 0
        res = 0
        nums.sort()
        for i in range(n):
            res += self.twoSumSmaller(nums, i+1, target - nums[i])
        return res

    def twoSumSmaller(self, nums, start, target):
        cnt = 0
        i = start
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] < target:
                cnt += (j-i) # IMPORTANT
                i += 1
            else:
                j -= 1
        return cnt

    # O(n^3) Solution
    def threeSumSmaller(self, nums, target):
        n = len(nums)
        if not nums or n < 3:
            return 0
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                new_target = target - (nums[i] + nums[j])
                ks = self.findK(nums, j+1, new_target)
                res += ks
        return res

    def findK(self, nums, start, target):
        cnt = 0
        for i in range(start, len(nums)):
            if nums[i] < target:
                cnt += 1
        return cnt
