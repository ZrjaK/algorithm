# 题目：419.甲板上的战舰
# 难度：MEDIUM
# 最后提交：2022-04-27 22:02:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans, n, m = 0, len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j]=="X" and (i==0 or board[i-1][j]== ".") and (j==0 or board[i][j-1]=="."):
                    ans += 1
        return ans