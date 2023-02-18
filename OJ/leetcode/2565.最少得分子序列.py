# 题目：2565.最少得分子序列
# 难度：HARD
# 最后提交：2023-02-12 11:40:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        s = "#" + s + "#"
        t = "#" + t + "#"
        h = []
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                h.append(i)
                i -= 1
                j -= 1
            else:
                i -= 1
        si = 0
        ans = len(t)
        for i in range(len(t)):
            while si < len(s) and s[si] != t[i]:
                si += 1
            while h and si >= h[-1]:
                h.pop()
            if si < len(s):
                # print(si, i, h)
                ans = min(ans, len(t) - len(h) - i - 1)
            else:
                break
            si += 1
        # print()
        return max(0, ans)