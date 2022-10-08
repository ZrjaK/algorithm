# 题目：529.扫雷游戏
# 难度：MEDIUM
# 最后提交：2022-07-29 02:29:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def calc(i, j):
            res = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0<=i+dx<m and 0<=j+dy<n and board[i+dx][j+dy] == "M":
                        res += 1
            return res
        m, n = len(board), len(board[0])
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        t = calc(click[0], click[1])
        if board[click[0]][click[1]] == "E" and t:
            board[click[0]][click[1]] = str(t)
            return board
        q = deque([[click[0], click[1]]])
        visited = set()
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            t = calc(x, y)
            if t:
                board[x][y] = str(t)
                continue
            board[x][y] = "B"
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0<=x+dx<m and 0<=y+dy<n:
                        q.append([x+dx, y+dy])
        return board