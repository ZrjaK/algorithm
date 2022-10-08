# 题目：952.按公因数计算最大组件大小
# 难度：HARD
# 最后提交：2022-09-27 08:34:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        parent = list(range(10**5+1))
        cnt = [0] * (10**5+1)
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            x, y = find(i), find(j)
            if x != y:
                cnt[y] += cnt[x]
                parent[x] = parent[y]
        d = defaultdict(list)
        for i in nums:
            cnt[i] += 1
        for i in nums:
            for j in range(1, ceil(i**0.5)+1):
                if i % j == 0:
                    if j > 1:
                        union(j, i)
                    if i//j > 1:
                        union(i//j, i)
        return max(cnt)
        