"""
Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently
used item before inserting a new item. For the purpose of this problem, when
there is a tie (i.e., two or more keys that have the same frequency), the least
recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?
"""
from collections import defaultdict, OrderedDict
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.remain = capacity
        self.freq_map = defaultdict(OrderedDict)
        self.node_map = {}
        self.least_freq = 1

    def _update(self, key, newVal=None):
        val, freq = self.node_map[key]
        if newVal is not None:
            val = newVal
        self.freq_map[freq].pop(key)
        if len(self.freq_map[self.least_freq]) == 0:
            self.least_freq += 1
        self.freq_map[freq+1][key] = (val, freq+1)
        self.node_map[key] = (val, freq+1)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map:
            return -1
        self._update(key)
        return self.node_map[key][0]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.node_map:
            self._update(key, value)
        else:
            self.node_map[key] = (value, 1)
            self.freq_map[1][key] = (value, 1)
            if self.remain == 0:
                # dict.popitem returns (key, value) pair
                removed = self.freq_map[self.least_freq].popitem(last=False)
                self.node_map.pop(removed[0])
            else:
                self.remain -= 1
            self.least_freq = 1 # reset to 1 after adding new item

    def traverse(self):
        for key, (value, freq) in self.node_map:
            print key, value, freq
