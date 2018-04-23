"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.

Have you met this question in a real interview?
Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1.
"""
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if not A or not target:
            return -1
        a = A
        l = 0
        r = len(a) - 1
        while l+1 < r:
            m = (l+r)/2
            if a[m] > a[r]:
                if target == a[m]:
                    return m
                elif a[l] <= target < a[m]:
                    r = m
                else:
                    l = m

            else:
                if target == a[m]:
                    return m
                elif a[m] < target <= a[r]:
                    l = m
                else:
                    r = m

        if a[l] == target:
            return l
        if a[r] == target:
            return r
        return -1
