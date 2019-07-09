"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
"""
解题思路：两个链表从头开始逐个比较，直到某一链表遍历完，另一链表剩下的部分就是末尾
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        p1 = l1
        p2 = l2
        result_head = None
        result_tail = None
        while (p1 is not None and p2 is not None):
            if p1.val <= p2.val:
                smaller = p1
                p1 = p1.next
            else:
                smaller = p2
                p2 = p2.next
            
            if result_head is None:
                result_head = smaller
                result_tail = result_head
            else:
                result_tail.next = smaller
                result_tail = result_tail.next

        if p1 is not None:
            result_tail.next = p1
        if p2 is not None:
            result_tail.next = p2
        return result_head