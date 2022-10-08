# 题目：999.可以被一步捕获的棋子数
# 难度：EASY
# 最后提交：2021-11-03 19:17:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        output = 0
        col = None
        row = None
        for i in range(len(board)):
            if 'R' in board[i]:
                row = i
                break
        col = board[row].index('R')
        s = ''.join(board[row])
        s = s.replace('.', '')
        if 'pR' in s:
            output += 1
        if 'Rp' in s:
            output += 1
        s = ''.join([i[col] for i in board])
        s = s.replace('.', '')
        if 'pR' in s:
            output += 1
        if 'Rp' in s:
            output += 1
        return output