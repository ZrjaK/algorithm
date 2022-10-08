# 题目：1857.有向图中最大颜色值
# 难度：HARD
# 最后提交：2022-09-28 13:50:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        d = defaultdict(list)
        degree = [0] * n
        for i, j in edges:
            d[i].append(j)
            degree[j] += 1
        found = 0
        f = [[0] * 26 for _ in range(n)]
        q = deque([i for i in range(n) if not degree[i]])
        while q:
            found += 1
            i = q.popleft()
            f[i][ord(colors[i])-97] += 1
            for j in d[i]:
                degree[j] -= 1
                for k in range(26):
                    f[j][k] = max(f[i][k], f[j][k])
                if not degree[j]:
                    q.append(j)
        if found != n:
            return -1
        ans = 0
        for i in range(n):
            ans = max(ans, max(f[i]))
        return ans