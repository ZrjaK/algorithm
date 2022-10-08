# 题目：1542.找出最长的超赞子字符串
# 难度：HARD
# 最后提交：2022-09-26 10:55:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestAwesome(self, s: str) -> int:
        h = {}
        h[0] = -1
        n = len(s)
        state = 0
        ans = 1
        for i in range(n):
            state ^= 1<<ord(s[i])-48
            if state in h:
                ans = max(ans, i-h[state])
            else:
                h[state] = i
            for k in range(10):
                t = state ^ 1<<k
                if t in h:
                    ans = max(ans, i-h[t])
        return ans