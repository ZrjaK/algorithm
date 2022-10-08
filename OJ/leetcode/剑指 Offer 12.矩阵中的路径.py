# 题目：剑指 Offer 12.矩阵中的路径
# 难度：MEDIUM
# 最后提交：2022-09-30 11:21:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        v = set()
        def check(i, j, p):
            if board[i][j] != word[p]:
                return False
            if p == len(word) - 1:
                return True
            v.add((i, j))
            for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0<=x<m and 0<=y<n and (x, y) not in v and check(x, y, p+1):
                    return True
            v.remove((i, j))
            return False
        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True
        return False
