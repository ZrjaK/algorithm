# 题目：909.蛇梯棋
# 难度：MEDIUM
# 最后提交：2022-08-02 18:18:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board = board[::-1]
        for i in range(n):
            if i % 2:
                board[i] = board[i][::-1]
        d = defaultdict(int)
        for i in range(n):
            for j in range(n):
                if board[i][j] != -1:
                    d[i*n+j+1] = board[i][j]
        v = set()
        q = deque([[0, 1]])
        res = [-1] * (n**2+1)
        while q:
            s, t = q.popleft()
            if t in v:
                continue
            v.add(t)
            res[t] = s
            for i in range(t+1, min(t+7, n**2+1)):
                if i not in d:
                    q.append([s+1, i])
                else:
                    q.append([s+1, d[i]])
        return res[-1]
