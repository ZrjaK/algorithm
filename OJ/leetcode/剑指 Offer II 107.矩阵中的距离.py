# 题目：剑指 Offer II 107.矩阵中的距离
# 难度：MEDIUM
# 最后提交：2022-10-10 16:45:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    q.append([0, i, j])
        ans = [[0] * n for _ in range(m)]
        v = set()
        while q:
            s, x, y = q.popleft()
            if (x, y) in v:
                continue
            v.add((x, y))
            ans[x][y] = s
            for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if 0<=nx<m and 0<=ny<n:
                    q.append((s+1, nx, ny))
        return ans