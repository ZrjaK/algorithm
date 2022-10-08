# 题目：36.有效的数独
# 难度：MEDIUM
# 最后提交：2022-09-06 08:50:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    board[i][j] = int(board[i][j])
        def check(x, y):
            d = [1] * 10
            for i in range(9):
                if board[i][y] == ".":
                    continue
                if not d[board[i][y]]:
                    return False
                else:
                    d[board[i][y]] -= 1
            d = [1] * 10
            for j in range(9):
                if board[x][j] == ".":
                    continue
                if not d[board[x][j]]:
                    return False
                else:
                    d[board[x][j]] -= 1
            return True
        for i in range(9):
            for j in range(9):
                if not check(i, j):
                    print("1", i, j)
                    return False
        def check2(x, y):
            d = [1] * 10
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] == ".":
                        continue
                    if  not d[board[i][j]]:
                        return False
                    else:
                        d[board[i][j]] -= 1
            return True
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check2(i, j):
                    return False
        return True
            