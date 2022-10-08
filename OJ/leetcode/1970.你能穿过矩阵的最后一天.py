# 题目：1970.你能穿过矩阵的最后一天
# 难度：HARD
# 最后提交：2022-09-19 23:13:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def p(x):
            h = [[0] * col for _ in range(row)]
            for i in range(x):
                h[cells[i][0]-1][cells[i][1]-1] = 1
            q = deque([[0, i] for i in range(col) if h[0][i] != 1])
            v= set()
            while q:
                x, y = q.popleft()
                if x == row-1:
                    return True
                if (x, y) in v:
                    continue
                v.add((x, y))
                for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                    if 0<=nx<row and 0<=ny<col and not h[nx][ny]:
                        q.append([nx, ny])
            return False
        l, r = 0, row * col
        while l <= r:
            mid = l+r>>1
            if not p(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r