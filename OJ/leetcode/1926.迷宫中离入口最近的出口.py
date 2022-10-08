# 题目：1926.迷宫中离入口最近的出口
# 难度：MEDIUM
# 最后提交：2022-08-12 01:10:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque([(0, entrance[0], entrance[1])])
        v = set()
        while q:
            s, x, y = q.popleft()
            if (x, y) in v:
                continue
            v.add((x, y))
            if x == 0 or x == m-1 or y == 0 or y == n-1:
                if not (x == entrance[0] and y == entrance[1]):
                    return s
            for dx, dy in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if 0<=dx<m and 0<=dy<n and maze[dx][dy] != "+":
                    q.append((s+1, dx, dy))
        return -1