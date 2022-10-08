# 题目：1638.统计只差一个字符的子串数目
# 难度：MEDIUM
# 最后提交：2022-07-19 03:24:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        for l in range(1, 1+min(len(s), len(t))):
            for i in range(len(s)-l+1):
                for j in range(len(t)-l+1):
                    c = 0
                    x, y = i, j
                    while x < i + l:
                        if s[x] != t[y]:
                            c += 1
                        x += 1
                        y += 1
                    ans += 1 if c == 1 else 0
        return ans