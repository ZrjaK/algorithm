# 题目：剑指 Offer 05.替换空格
# 难度：EASY
# 最后提交：2022-09-30 11:03:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")