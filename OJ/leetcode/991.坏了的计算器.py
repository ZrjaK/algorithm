# 题目：991.坏了的计算器
# 难度：MEDIUM
# 最后提交：2022-09-06 23:11:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while startValue < target:
            if not target & 1:
                target //= 2
                ans += 1
            else:
                target = (target+1) // 2
                ans += 2
        return ans + startValue - target