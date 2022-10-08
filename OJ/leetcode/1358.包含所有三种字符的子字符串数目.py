# 题目：1358.包含所有三种字符的子字符串数目
# 难度：MEDIUM
# 最后提交：2022-05-23 11:06:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        d = defaultdict(int)
        l = 0
        ans = 0
        for r in range(n):
            d[s[r]] +=  1
            while d["a"] >= 1 and d["b"] >= 1 and d["c"] >= 1:
                ans += n-r
                d[s[l]] -= 1
                l += 1
        return ans