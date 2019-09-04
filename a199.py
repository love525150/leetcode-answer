# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        self._traversal(root, l, 0)
        return l
        
    def _traversal(self, node, l, level):
        if node is None:
            return
        if len(l) - 1 < level:
            l.append(node.val)
        else:
            l[level] = node.val
        self._traversal(node.left, l, level + 1)
        self._traversal(node.right, l, level + 1)