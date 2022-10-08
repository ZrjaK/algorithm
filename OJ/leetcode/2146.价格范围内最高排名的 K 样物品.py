# 题目：2146.价格范围内最高排名的 K 样物品
# 难度：MEDIUM
# 最后提交：2022-08-13 16:48:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = []
        q = deque([(0, start[0], start[1])])
        h = [[0] * n for _ in range(m)]
        v = set()
        while q:
            s, x, y = q.popleft()
            if (x, y) in v:
                continue
            v.add((x, y))
            if pricing[0] <= grid[x][y] <= pricing[1]:
                res.append([x, y])
                h[x][y] = s
            for dx, dy in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if 0<=dx<m and 0<=dy<n and grid[dx][dy]:
                    q.append((s+1, dx, dy))
        res.sort(key=lambda x: (h[x[0]][x[1]], grid[x[0]][x[1]], x[0], x[1]))
        return res[:k]