'''
给定一个二叉树，返回它的中序遍历。
使用迭代算法完成
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        l = []
        cur = root
        while cur or len(stack):
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            l.append(cur.val)
            cur = cur.right
        
        return l

