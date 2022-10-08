# 题目：剑指 Offer 50.第一个只出现一次的字符
# 难度：EASY
# 最后提交：2022-10-03 18:49:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def firstUniqChar(self, s: str) -> str:
        c = Counter(s)
        for i in s:
            if c[i] == 1:
                return i
        return " "