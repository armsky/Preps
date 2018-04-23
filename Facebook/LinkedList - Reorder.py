"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        a = ListNode(None)
        a.next = head
        b = ListNode(None)
        b.next = head
        while b and b.next:
            a = a.next
            b = b.next.next
        second_head = a.next
        a.next = None
        a = second_head
        b = head

        a = self.reverse(a)
        self.merge(a, b)

    def merge(self, a, b):
        # b is longer than a
        dummy = ListNode(None)
        dummy.next = b
        while a:
            t = b.next
            b.next = a
            a = a.next
            b.next.next = t
            b = t
        return dummy.next

    def reverse(self, a):
        pre = None
        cur = a
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
