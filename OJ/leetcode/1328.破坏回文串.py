# 题目：1328.破坏回文串
# 难度：MEDIUM
# 最后提交：2022-09-07 08:19:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l = list(palindrome)
        for i in range(len(l)//2):
            if ord(l[i]) > 97:
                l[i] = "a"
                break
        else:
            if len(l) == 1:
                return ""
            else:
                l[-1] = "b"
        return "".join(l)