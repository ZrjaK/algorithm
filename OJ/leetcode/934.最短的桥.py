# 题目：934.最短的桥
# 难度：MEDIUM
# 最后提交：2022-08-03 20:28:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        source = collections.deque()
        m = len(A)
        n = len(A[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or A[i][j] == 0: return
            A[i][j] = 0
            source.append((i, j))
            for (r, c) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                dfs(r, c)
        find = False
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and not find:
                    dfs(i,j)
                    find = True
        seen = set(source)
        level = 0
        while source:
            size = len(source)
            for s in range(size):
                i,j = source.popleft()
                for r,c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if r< 0 or c < 0 or r >= m or c >= n or (r,c) in seen: continue
                    if A[r][c] == 0:
                        source.append((r,c))
                        seen.add((r,c))
                    else:
                        return level
            level += 1
        return level