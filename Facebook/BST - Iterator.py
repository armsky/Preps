"""
Implement an iterator over a binary search tree (BST). Your iterator will be
initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory,
where h is the height of the tree.
"""
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.q = []
        self.reload(root)

    def reload(self, node):
        while node:
            self.q.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.q

    def next(self):
        """
        :rtype: int
        """
        node = self.q.pop()
        self.reload(node.right)
        return node.val
