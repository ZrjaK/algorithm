# 题目：剑指 Offer II 119.最长连续序列
# 难度：MEDIUM
# 最后提交：2022-10-10 22:08:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        d = {v: i for i, v in enumerate(nums)}
        n = len(nums)
        uf = UnionFind(n)
        v = set()
        for i in range(n):
            if nums[i]-1 in v:
                uf.union(i, d[nums[i]-1])
            if nums[i]+1 in v:
                uf.union(i, d[nums[i]+1])
            v.add(nums[i])
        return max(uf.size + [0])


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.part = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        x, y = self.find(i), self.find(j)
        if x != y:
            self.size[y] += self.size[x]
            self.parent[x] = self.parent[y]
            self.part -= 1
