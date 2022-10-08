# 题目：1234.替换子串得到平衡字符串
# 难度：MEDIUM
# 最后提交：2022-05-22 23:13:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        avg = n // 4
        c = Counter(s)
        l = 0
        ans = n
        for r in range(n):
            c[s[r]] -= 1
            while l < n and c["Q"] <= avg and c["W"] <= avg and c["E"] <= avg and c["R"] <= avg:
                ans = min(ans, r-l+1)
                c[s[l]] += 1
                l += 1
        return ans