# 题目：2119.反转两次的数字
# 难度：EASY
# 最后提交：2023-01-16 10:40:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == int(str(int(str(num)[::-1]))[::-1])