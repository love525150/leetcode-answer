'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''
'''
核心：
1、链表的遍历
2、进位的处理
3、不等长用0补齐
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        result_head = None
        result_pointer = result_head
        carry = 0
        padding_node = ListNode(0)
        while p1 is not None or p2 is not None or carry == 1:
            if p1 is None: p1 = padding_node
            if p2 is None: p2 = padding_node
            v = p1.val + p2.val + carry
            if v > 9:
                v = v - 10
                carry = 1
            else:
                v = v
                carry = 0
            new_node = ListNode(v)
            if result_head is None:
                result_head = new_node
                result_pointer = new_node
            else:
                result_pointer.next = new_node
                result_pointer = result_pointer.next
            
            p1 = p1.next
            p2 = p2.next

        return result_head