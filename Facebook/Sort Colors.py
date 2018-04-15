"""
Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red, white
and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""

class Solution(object):
    # One pass solution
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        redest = 0
        bluest = len(nums) - 1
        i = 0
        while i < bluest + 1: #right bound is bluest
            if nums[i] == 0:
                nums[i], nums[redest] = nums[redest], nums[i]
                redest += 1
                i += 1
                continue
            if nums[i] == 2:
                nums[i], nums[bluest] = nums[bluest], nums[i]
                bluest -= 1 # Do not update i
                continue

            i += 1
