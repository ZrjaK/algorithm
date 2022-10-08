# 题目：2076.处理含限制条件的好友请求
# 难度：HARD
# 最后提交：2022-09-20 23:13:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        d = [1<<i for i in range(n)]
        parent = list(range(n))
        r = [0] * n
        for i, j in restrictions:
            r[i] |= 1<<j
            r[j] |= 1<<i
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            i, j = find(i), find(j)
            d[j] |= d[i]
            r[j] |= r[i]
            parent[i] = parent[j]
        ans = []
        for i, j in requests:
            x, y = find(i), find(j)
            if not d[x] & r[y] and not d[y] & r[x]:
                union(i, j)
                ans.append(True)
            else:
                ans.append(False)
        return ans