'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
'''
'''
使用有界队列，队列大小为n+1，遍历链表的时候不停向队列里添加节点，遍历完成后，队列的头就是倒数第n+1个节点，队列第二个就是倒数第n个节点
本质上就是使得遍历到链表终点时，能够拿到倒数第n+1个节点
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        q = deque(maxlen = n + 1)
        current = head
        length = 0
        while current is not None:
            q.append(current)
            current = current.next
            length += 1
        
        if length == n: # 删除的是头节点
            return head.next

        beforeN = q.popleft()
        n = q.popleft()
        beforeN.next = n.next

        return head