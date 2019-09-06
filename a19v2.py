'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
'''
'''
本质上就是使得遍历到链表终点时，能够拿到倒数第n+1个节点
遍历到终点时，倒数第n+1个节点离终点（null）差n+1个节点，因此可以用一个遍历开始就相差n+1个节点的第二指针来指示
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        n0 = ListNode(0) # 头节点前加一个虚节点，防止被删除的是头节点时的异常(因为这里处理的是倒数的节点，前面加节点不影响)
        n0.next = head
        p1 = n0
        p2 = n0
        for i in range(n + 1):
            p1 = p1.next # 使得p1，p2相差n+1个节点
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return n0.next