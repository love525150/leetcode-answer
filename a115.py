'''
给定一个二叉树，返回它的 后序 遍历。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        l = []
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            l.insert(0, cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:    
                stack.append(cur.right)

        return l