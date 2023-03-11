# 题目：2581.统计可能的树根数目
# 难度：HARD
# 最后提交：2023-03-05 00:22:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        d = [[] for _ in range(n)]
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        g = set((i, j) for i, j in guesses)
        c = [0] * n
        rc = [0] * n
        def dfs1(i, fa):
            for j in d[i]:
                if j == fa:
                    continue
                dfs1(j, i)
                c[i] += c[j]
                if (i, j) in g:
                    c[i] += 1
        dfs1(0, -1)
        def dfs2(i, fa):
            for j in d[i]:
                if j == fa:
                    continue
                if (j, i) in g:
                    rc[j] += 1
                rc[j] += rc[i] + c[i] - c[j] - int((i, j) in g)
                dfs2(j, i)
        dfs2(0, -1)
        ans = 0
        for i, j in zip(c, rc):
            if i + j >= k:
                ans += 1
        # for i in rc:
        #     if i >= k:
        #         ans += 1
        return ans
                
            