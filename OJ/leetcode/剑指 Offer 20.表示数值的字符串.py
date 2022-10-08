# 题目：剑指 Offer 20.表示数值的字符串
# 难度：MEDIUM
# 最后提交：2022-10-01 16:43:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False