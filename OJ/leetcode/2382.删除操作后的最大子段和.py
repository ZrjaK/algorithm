# 题目：2382.删除操作后的最大子段和
# 难度：HARD
# 最后提交：2022-08-21 00:33:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        h = list(accumulate(nums)) + [0]
        n = len(nums)
        parent = list(range(n))
        s = [0] * n
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            s[find(j)] += s[find(i)]
            parent[find(i)] = parent[find(j)]
        v = set()
        res = []
        ma = 0
        for i in removeQueries[::-1]:
            res.append(ma)
            s[i] = nums[i]
            ma = max(ma, s[find(i)])
            if i-1 in v:
                union(i-1, i)
                ma = max(ma, s[find(i)])
            if i+1 in v:
                union(i, i+1)
                ma = max(ma, s[find(i+1)])
            v.add(i)
        return res[::-1]