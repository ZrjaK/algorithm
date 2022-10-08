# 题目：854.相似度为 K 的字符串
# 难度：HARD
# 最后提交：2022-09-21 08:28:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n = len(s1)
        q = deque([(0, s1)])
        v = set()
        while q:
            s, t = q.popleft()
            if t == s2:
                return s
            if t in v:
                continue
            v.add(t)
            for i in range(n):
                if t[i] != s2[i]:
                    break
            for j in range(i+1, n):
                if t[j] == s2[i] != s2[j]:
                    f = list(t)
                    f[i], f[j] = f[j], f[i]
                    q.append((s+1, "".join(f)))
