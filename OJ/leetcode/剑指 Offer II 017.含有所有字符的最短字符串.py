# 题目：剑指 Offer II 017.含有所有字符的最短字符串
# 难度：HARD
# 最后提交：2022-10-05 10:55:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        f = Counter(t)
        l = 0
        c = Counter()
        ans = "a" * 10**6
        for r in range(len(s)):
            c[s[r]] += 1
            while all(c[i] >= f[i] for i in f):
                if r-l+1 < len(ans):
                    ans = s[l:r+1]
                c[s[l]] -= 1
                l += 1
        return ans if ans != "a" * 10**6 else ""