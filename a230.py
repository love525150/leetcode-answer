'''
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
'''
'''
解题思路：搜索二叉树的中序遍历就是按序遍历二叉树
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        return self.midTravel(root, k)
    
    def midTravel(self, node, k):
        if node.left:
            v = self.midTravel(node.left, k)
            if v is not None:
                return v
        self.count += 1
        if self.count == k:
            return node.val
        if node.right:
            v = self.midTravel(node.right, k)
            if v is not None:
                return v