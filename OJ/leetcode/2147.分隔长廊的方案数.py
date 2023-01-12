# 题目：2147.分隔长廊的方案数
# 难度：HARD
# 最后提交：2023-01-03 22:08:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ans, c, pre = 1, 0, 0
        for i, ch in enumerate(corridor):
            if ch == 'S':
                c += 1
                if c > 2 and c % 2:
                    ans *= i - pre
                    ans %= int(1e9+7)
                pre = i
        return ans if c and c % 2 == 0 else 0