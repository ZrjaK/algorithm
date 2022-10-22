# 题目：1998.数组的最大公因数排序
# 难度：HARD
# 最后提交：2022-10-17 15:26:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def gcdSort(self, nums: List[int]) -> bool: 
        n = len(nums)
        d = defaultdict(list)
        for i in range(n):
            for j in range(1, int(nums[i]**0.5)+1):
                if not nums[i] % j:
                    if j != 1:
                        d[j].append(i)
                    if j != nums[i]//j:
                        d[nums[i]//j].append(i)
        uf = UnionFind(n)
        for f in d:
            for i in d[f]:
                uf.union(d[f][0], i)
        d = defaultdict(list)
        for i in range(n):
            d[uf.find(i)].append(i)
        for i in d:
            h = [nums[j] for j in d[i]]
            print(h, d[i])
            h.sort(reverse=True)
            for j in d[i]:
                nums[j] = h.pop()
        return sorted(nums) == nums


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
