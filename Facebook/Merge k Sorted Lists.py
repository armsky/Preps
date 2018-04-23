"""
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

Have you met this question in a real interview?
Example
Given lists:

[
  2->4->null,
  null,
  -1->null
],
return -1->2->4->null.
"""
from heapq import heappop, heappush

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if not lists:
            return None
        q = []
        dummy_head = ListNode(None)
        for node in lists:
            if node:
                heappush(q, (node.val, node))
        cur = dummy_head
        while q:
            node = heappop(q)[1]
            if node.next:
                heappush(q, (node.next.val, node.next))
            cur.next = node
            cur = cur.next

        return dummy_head.next
