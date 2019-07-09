'''
反转一个单链表
'''
'''
解题思路：链表的从尾部开始构造
node = ListNode(p.val)
node.next = r
r = node
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = list()
        p = head
        r = None
        while p is not None:
            if r is None:
                r = ListNode(p.val)
            else:
                node = ListNode(p.val)
                node.next = r
                r = node
            p = p.next
        
        return r
