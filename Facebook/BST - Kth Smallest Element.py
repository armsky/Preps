"""
Given a binary search tree, write a function kthSmallest to find the kth smallest
element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to
find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
class Solution(object):

    # Recursively
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cnt = 0
        self.res = None
        self.visit(root, 0, k)
        return self.res

    def visit(self, root, cnt, k):
        if not root or cnt == k:
            return
        self.visit(root.left, cnt, k)
        self.cnt += 1
        if self.cnt == k:
            self.res = root.val
            return
        self.visit(root.right, cnt, k)
