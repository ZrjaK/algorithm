# 题目：剑指 Offer II 019.最多删除一个字符得到回文
# 难度：EASY
# 最后提交：2022-10-05 11:05:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(x, y):
            while x < y:
                if s[x] != s[y]:
                    return False
                x += 1
                y -= 1
            return True
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] != s[r]:
                return check(l + 1, r) or check(l, r - 1)
            l += 1
            r -= 1
        return True