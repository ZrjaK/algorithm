# 题目：2370.最长理想子序列
# 难度：MEDIUM
# 最后提交：2022-08-07 10:50:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        d = defaultdict(int)
        for i in s:
            t = ord(i)
            f = False
            for j in range(max(97, t-k), min(t+k+1, 97+26)):
                # if d[j]:
                #     f = True
                d[t] = max(d[t],d[j])
            # if f :
            d[t] += 1
        ans = 0
        for j in range(97, 97+26):
            ans = max(ans, d[j])
        return ans