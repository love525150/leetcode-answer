'''
给定一个二叉树，返回它的中序遍历。
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
        result_list = []
        self._receiveTraversal(root, result_list)
        return result_list        

    def _receiveTraversal(self, node, result_list):
        if node is None:
            return
            
        if node.left is not None:
            self._receiveTraversal(node.left, result_list)
        
        result_list.append(node.val)

        if node.right is not None:
            self._receiveTraversal(node.right, result_list)
