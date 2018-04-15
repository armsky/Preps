"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
Have you met this question in a real interview?
Example
An example:

  2
 / \
1   4
   / \
  3   5
The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    #NOTE: Use max and min
    class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        minv = -0xffffffff
        maxv = 0xffffffff
        return self.isValid(root, minv, maxv)


    def isValid(self, root, minv, maxv):
        if not root:
            return True
        if self.isValid(root.left, minv, root.val) and self.isValid(root.right, root.val, maxv) and minv < root.val < maxv:
            return True
        return False

    # NOTE: Inorder traversal, track last value
    def isValidBST(self, root):
        self.lastVal = None
        self.isBST = True
        self.isValid(root)
        return self.isBST


    def isValid(self, root):
        if not root:
            return
        self.isValid(root.left)
        if self.lastVal is not None and root.val <= self.lastVal:
            self.isBST = False
            return
        self.lastVal = root.val
        self.isValid(root.right)
