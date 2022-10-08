# 题目：1784.检查二进制字符串字段
# 难度：EASY
# 最后提交：2022-10-03 00:53:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len([i for i in s.split("0") if i]) <= 1