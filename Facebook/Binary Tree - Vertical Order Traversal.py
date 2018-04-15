"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Have you met this question in a real interview?
Example
Given binary tree {3,9,20,#,#,15,7}

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
Return its vertical order traversal as:
[[9],[3,15],[20],[7]]

Given binary tree {3,9,8,4,0,1,7}

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
Return its vertical order traversal as:
[[4],[9],[3,0,1],[8],[7]]
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import defaultdict

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        res = defaultdict(list)
        q = [(root, 0)]
        while q:
            node, level = q.pop(0)
            if node:
                res[level] += [node.val]
                q.append((node.left, level-1))
                q.append((node.right, level+1))
        return [res[level] for level in sorted(res)]
