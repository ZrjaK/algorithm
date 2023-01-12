# 题目：2027.转换字符串的最少操作次数
# 难度：EASY
# 最后提交：2022-12-27 02:18:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        ans = 0
        while i < len(s):
            if s[i] == "X":
                i += 3
                ans += 1
            else:
                i += 1
        return ans
            