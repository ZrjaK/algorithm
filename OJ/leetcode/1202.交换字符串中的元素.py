# 题目：1202.交换字符串中的元素
# 难度：MEDIUM
# 最后提交：2022-08-17 20:57:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = parent[find(j)]
        for i, j in pairs:
            union(i, j)
        d = defaultdict(list)
        for i in range(n):
            d[find(i)].append(i)
        for i in d.keys():
            d[i] = deque(sorted(d[i], key=lambda x:s[x]))
        ans = ""
        for i in range(n):
            ans += s[d[find(i)].popleft()]
        return ans