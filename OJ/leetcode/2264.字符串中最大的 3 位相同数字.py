# 题目：2264.字符串中最大的 3 位相同数字
# 难度：EASY
# 最后提交：2022-05-08 10:31:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            if str(i)*3 in num:
                return str(i)*3
        return ""