# 题目：1553.吃掉 N 个橘子的最少天数
# 难度：HARD
# 最后提交：2022-08-26 23:25:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDays(self, n: int) -> int:
        q = deque([(0, n)])
        v = set()
        while q:
            s, t = q.popleft()
            if t in v:
                continue
            v.add(t)
            if not t:
                return s
            if t % 2 == 0:
                q.append((s+1, t//2))
            if t % 3 == 0:
                q.append((s+1, t//3))
            q.append((s+1, t-1))