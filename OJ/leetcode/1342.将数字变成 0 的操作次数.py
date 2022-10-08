# 题目：1342.将数字变成 0 的操作次数
# 难度：EASY
# 最后提交：2022-08-26 21:09:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            if num & 1:
                ans += 1
            ans += 1
            num >>= 1
        return max(ans - 1, 0)