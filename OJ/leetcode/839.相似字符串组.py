# 题目：839.相似字符串组
# 难度：HARD
# 最后提交：2022-09-16 09:32:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = list(range(n))
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = parent[find(j)]
        def check(s, t):
            res = len([1 for i, j in zip(s, t) if i != j])
            return res == 0 or res == 2
        for i in range(n):
            for j in range(i):
                if check(strs[i], strs[j]):
                    union(i, j)
        v = set()
        for i in range(n):
            v.add(find(i))
        return len(v)