# 题目：818.赛车
# 难度：HARD
# 最后提交：2022-10-14 11:39:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 0, 1)])
        v = set()
        while q:
            x, p, s = q.popleft()
            if p == target:
                return x
            if (p, s) in v:
                continue
            v.add((p, s))
            q.append((x+1, p+s, s*2))
            if s > 0:
                q.append((x+1, p, -1))
            else:
                q.append((x+1, p, 1))
        