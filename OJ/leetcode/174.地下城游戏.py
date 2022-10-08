# 题目：174.地下城游戏
# 难度：HARD
# 最后提交：2022-04-09 13:41:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        @lru_cache(None)
        def p(row, col):
            if row == len(dungeon)-1 and col == len(dungeon[0])-1:
                return 1 + abs(dungeon[row][col]) if dungeon[row][col] < 0 else 1
            if row == len(dungeon)-1:
                return max(1, p(row, col+1) - dungeon[row][col])
            if col == len(dungeon[0])-1:
                return max(1, p(row+1, col) - dungeon[row][col])
            return max(1, min(p(row+1, col), p(row, col+1)) - dungeon[row][col])
        return p(0, 0)