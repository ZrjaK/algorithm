# 题目：2484.统计回文子序列数目
# 难度：HARD
# 最后提交：2022-11-27 12:04:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPalindromes(self, s: str) -> int:
        d = {i: defaultdict(int) for i in range(5)}
        ans = 0
        d[0][""] = 1
        for i in s:
            for j in "0123456789":
                for k in "0123456789":
                    t = i+j+k+j
                    if t in d[4]:
                        ans += d[4][t]
                        ans %= 10**9+7
            for k in range(3, -1, -1):
                for j in d[k]:
                    d[k+1][j+i] += d[k][j]
        return ans
