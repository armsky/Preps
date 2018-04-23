"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    res = []
    def binaryTreePaths(self, root):
        if not root:
            return self.res
        self.getPath(root, str(root.val))
        return self.res

    def getPath(self, root, path):
        if not root.left and not root.right:
            self.res.append(path)
            return
        if root.left:
            self.getPath(root.left, path+'->'+str(root.left.val))
        if root.right:
            self.getPath(root.right, path+'->'+str(root.right.val))
