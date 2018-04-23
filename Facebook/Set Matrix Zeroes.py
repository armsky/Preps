"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""
class Solution(object):
    # A O(1) solution:
    # 1. use col0 record should set matrix[i][0] to be 0 at last
    # 2. if matrix[i][j]==0, set matrix[i][0] and matrix[0][j] to 0
    # 3. bottom up set all other 0s if matrix[i][0] or matrix[0][j] is 0
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        col0 = 1
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, n):   # do not change when j==0
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, 0, -1): # j will be range from [1:n]
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
