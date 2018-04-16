"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?
"""
#NOTE: Easy implementation by using OrderedDict
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.remain = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            if self.remain == 0:
                self.cache.popitem(last=False)
            else:
                self.remain -= 1

#NOTE: Regular implementation - map + doublly linked list
class Node(object):

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {} #{key: node}
        self.capacity = capacity
        self.len = 0
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.pre = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._moveToTail(node)
            return node.val
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.map:
            node = Node(key, value)
            self.map[key] = node
            if self.len < self.capacity:
                self.len += 1
            else:
                del self.map[self.head.next.key]
                self._remove(self.head.next)
            self._moveToTail(node)
        else:
            node = self.map[key]
            self._remove(node)
            node.val = value
            self._moveToTail(node)


    def _moveToTail(self, node):
        node.pre = self.tail.pre
        node.pre.next = node
        self.tail.pre = node
        node.next = self.tail


    def _remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
