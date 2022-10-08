# 题目：剑指 Offer II 032.有效的变位词
# 难度：EASY
# 最后提交：2022-10-06 02:22:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) and s != t