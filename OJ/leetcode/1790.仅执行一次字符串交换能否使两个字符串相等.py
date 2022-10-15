# 题目：1790.仅执行一次字符串交换能否使两个字符串相等
# 难度：EASY
# 最后提交：2022-10-11 00:10:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        def check(s, t):
            h = list(s)
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    h[i], h[j] = h[j], h[i]
                    if "".join(h) == t:
                        return True
                    h[i], h[j] = h[j], h[i]
            return False
        return s1 == s2 or check(s1, s2) or check(s2, s1)