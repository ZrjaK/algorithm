# 题目：2520.统计能整除数字的位数
# 难度：EASY
# 最后提交：2023-01-01 10:30:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        ans = 0
        for i in s:
            if num % int(i) == 0:
                ans += 1
        return ans