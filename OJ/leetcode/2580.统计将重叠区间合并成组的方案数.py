# 题目：2580.统计将重叠区间合并成组的方案数
# 难度：MEDIUM
# 最后提交：2023-03-04 22:38:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedList
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        n = len(ranges)
        ranges.sort()
        sl = SortedList([ranges[0][1]])
        dsu = DisjointSetUnion(n)
        for i in range(1, n):
            if ranges[i][0] <= sl[-1]:
                dsu.union(i-1, i)
            sl.add(ranges[i][1])
        return pow(2, dsu.num_sets, int(1e9+7))
        
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n
 
    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a
 
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
 
            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]
 
    def set_size(self, a):
        return self.size[self.find(a)]
 
    def __len__(self):
        return self.num_sets