"""
Given an array nums and a target value k, find the maximum length of a subarray
that sums to k. If there isn't one, return 0 instead.

 Notice
The sum of the entire nums array is guaranteed to fit within the 32-bit signed
integer range.

Have you met this question in a real interview?
Example
Given nums = [1, -1, 5, -2, 3], k = 3, return 4.

Explanation:
because the subarray [1, -1, 5, -2] sums to 3 and is the longest.
Given nums = [-2, -1, 2, 1], k = 1, return 2.

Explanation:
because the subarray [-1, 2] sums to 1 and is the longest.
Challenge
Can you do it in O(n) time?
"""
class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    #NOTE: 思路：用Map保存从0到i的sum及i。如果Sum是k，则为1个候选结果；如果Sum-k已经在Map中，
    #      则从Sum-k结束到i为一个候选，取所有候选中的最大长度。O(n)

    def maxSubArrayLen(self, nums, k):
        sum = 0
        maxlen = 0
        map = {}
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                maxlen = i + 1
            elif sum - k in map:
                maxlen = max(maxlen, i - map[sum-k])
            if sum not in map: # do not update if same sum value already in map
                map[sum] = i
        return maxlen
