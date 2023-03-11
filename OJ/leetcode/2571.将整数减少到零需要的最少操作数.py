# 题目：2571.将整数减少到零需要的最少操作数
# 难度：MEDIUM
# 最后提交：2023-02-21 20:10:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, n: int) -> int:
        logn = n.bit_length() + 1
        vis = [0] * (1 << logn + 2)
        q = [(0, n)]
        for s, x in q:
            if x == 0:
                return s
            for i in range(logn):
                t = x + (1 << i)
                if not vis[t]:
                    vis[t] = 1
                    q.append((s + 1, t))
                
                t = x - (1 << i)
                if not vis[t]:
                    vis[t] = 1
                    q.append((s + 1, t))