# 题目：9.回文数
# 难度：EASY
# 最后提交：2021-10-20 13:07:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False