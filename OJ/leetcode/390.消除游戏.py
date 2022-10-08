# 题目：390.消除游戏
# 难度：MEDIUM
# 最后提交：2022-04-18 08:08:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lastRemaining(self, n: int) -> int:
        ans = 1
        c = 1
        left = True
        while n > 1:
            if left or n % 2 == 1:
                ans += c
            left = not left
            c *= 2
            n //= 2
        return ans