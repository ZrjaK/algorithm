# 题目：464.我能赢吗
# 难度：MEDIUM
# 最后提交：2022-07-05 01:46:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def dfs(usedNumbers: int, currentTotal: int) -> bool:
            for i in range(1, maxChoosableInteger+1):
                if (usedNumbers >> i) & 1 == 0:
                    if currentTotal + i >= desiredTotal or not dfs(usedNumbers | (1 << i), currentTotal + i):
                        return True
            return False

        return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dfs(0, 0)