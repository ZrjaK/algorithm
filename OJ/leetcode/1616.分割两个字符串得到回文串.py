# 题目：1616.分割两个字符串得到回文串
# 难度：MEDIUM
# 最后提交：2022-06-12 13:15:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalindrome(s: str) -> bool:
            return s == s[::-1]

        def check(a: str, b: str) -> bool:
            left = 0
            while left <= len(a) // 2:
                if a[left] != b[-left - 1]:
                    break
                left += 1
            if left >= len(a) // 2:
                return True
            if isPalindrome(a[left: len(a) - left]) or isPalindrome(b[left: len(b) - left]):
                return True
            return False
        return check(a, b) or check(b, a)