design google map。
设计GeoHash，设计图，如何找出最近的公交线，耗时最短的公交线，
以及公交线每个bus的停靠时间的处理，注意bus高峰期和非高峰期 interval time是不一样的，
如何查找最近的一趟bus，我给的是binary search。


Build a map. Given location A and B, get the shortest time for the route. The
possible way could be Walking, Public transportation(considering the fare and ),
 driving ( pay attention to traffic direction). Think about how you are going to
 store all those stuff.

主要用到dijkstra's algorithm实现最短步行路径，geohash找最近的k个巴士站。
白板implement dijkstra's。如果一条巴士线有很多站，则需要用到binary search找到离source最近的巴士站点。

from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")
