# 题目：2516.每种字符至少取 K 个
# 难度：MEDIUM
# 最后提交：2022-12-25 19:01:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        c = Counter(s)
        if any(c[i] < k for i in "abc"):
            return -1
        s += s
        ans = n
        l, r = 0, n
        while l <= n:
            while any(c[i] < k for i in "abc"):
                c[s[r]] += 1
                r += 1
            ans = min(ans, r-l)
            c[s[l]] -= 1
            l += 1
        return ans