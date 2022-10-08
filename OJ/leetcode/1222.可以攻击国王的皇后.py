# 题目：1222.可以攻击国王的皇后
# 难度：MEDIUM
# 最后提交：2022-09-12 20:29:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        h = [[0] * 8 for _ in range(8)]
        for i, j in queens:
            h[i][j] = 1
        ans = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if not dx and not dy:
                    continue
                x, y = king
                while 0<=x<8 and 0<=y<8:
                    if h[x][y]:
                        ans.append([x, y])
                        break
                    x -= dx
                    y -= dy
        return ans