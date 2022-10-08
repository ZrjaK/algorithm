# 题目：剑指 Offer II 018.有效的回文
# 难度：EASY
# 最后提交：2022-10-05 10:59:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(i.lower() for i in s if i.isalpha() or i in "1234567890")
        return t == t[::-1]