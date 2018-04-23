"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path must
contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
class Solution(object):

    # NOTE: Good Solution O(n)
    # update res
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPath = -0xffffffff
        self.helper(root)
        return self.maxPath

    def helper(self, root):
        if not root:
            return 0
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        self.maxPath = max(self.maxPath, left + right + root.val)
        return max(left, right) + root.val

    # First attampt, got TLE
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPath = -0xffffffff
        self.helper(root)
        return self.maxPath

    def singleMaxPathSum(self, root):
        if not root:
            return -0xffffffff
        leftpath = self.singleMaxPathSum(root.left) + root.val
        rightpath = self.singleMaxPathSum(root.right) + root.val
        return max(root.val, leftpath, rightpath)

    def helper(self, root):
        if not root:
            return -0xffffffff
        leftmax = self.helper(root.left)
        rightmax = self.helper(root.right)
        leftsingle = self.singleMaxPathSum(root.left)
        rightsingle = self.singleMaxPathSum(root.right)
        # print root.val, leftmax, rightmax
        rootmax = max(root.val,
                      leftmax,
                      rightmax,
                      leftsingle + root.val,
                      rightsingle + root.val,
                      leftsingle + rightsingle + root.val)
        self.maxPath = max(self.maxPath, rootmax)
        return rootmax
