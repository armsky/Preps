"""
There are two sorted arrays A and B of size m and n respectively. Find the median
of the two sorted arrays.

Have you met this question in a real interview?
Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.

Given A=[1,2,3] and B=[4,5], the median is 3.
"""
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, B, n/2 + 1)
        else:
            smaller = self.findKth(A, B, n/2)
            bigger = self.findKth(A, B, n/2 + 1)
            return (smaller + bigger) / 2.0

    def findKth(self, a, b, k):
        if len(a) == 0:
            return b[k-1]
        if len(b) == 0:
            return a[k-1]
        if k == 1:
            return min(a[0], b[0])

        va = a[k/2 - 1] if len(a) >= k/2 else None
        vb = b[k/2 - 1] if len(b) >= k/2 else None

        if vb is None or (va and va < vb):
            return self.findKth(a[k/2:], b, k - k/2)
        else:
            return self.findKth(a, b[k/2:], k - k/2)
