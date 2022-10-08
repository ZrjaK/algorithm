# 题目：473.火柴拼正方形
# 难度：MEDIUM
# 最后提交：2022-07-05 01:55:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        target = sum(matchsticks) / 4
        if target != int(target):
            return False
        matchsticks.sort(reverse=True)
        if target < matchsticks[0]:
            return False
        def dfs(i, s):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if s[j] + matchsticks[i] <= target:
                    if j == 0 or s[j] != s[j-1]:
                        s[j] += matchsticks[i]
                        if dfs(i+1, s):
                            return True
                        s[j] -= matchsticks[i]
            return False
        return dfs(0, [0, 0, 0, 0])