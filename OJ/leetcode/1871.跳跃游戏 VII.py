# 题目：1871.跳跃游戏 VII
# 难度：MEDIUM
# 最后提交：2022-06-20 16:25:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [0] * n
        dp[-1] = 0 if s[-1] == "1" else 1
        suf = [dp[-1]] * n
        for i in range(n-2, -1, -1):
            if s[i] == "1" or i + minJump > n-1:
                suf[i] = suf[i+1] + dp[i]
                continue
            t = suf[i+minJump]-suf[i+maxJump+1] if i+maxJump+1 <= n-1 else suf[i+minJump]
            dp[i] = 1 if t > 0 else 0
            suf[i] = suf[i+1] + dp[i]
        return dp[0] == 1