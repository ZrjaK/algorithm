# 题目：1625.执行操作后字典序最小的字符串
# 难度：MEDIUM
# 最后提交：2022-08-11 08:29:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        ans = s
        q = deque([s])
        v = set()
        while q:
            t = q.popleft()
            if t in v:
                continue
            v.add(t)
            ans = min(ans ,t)
            q.append(t[-b:]+t[:-b])
            c = ""
            for i in range(n):
                if i % 2:
                    c += str((int(t[i])+a) % 10)
                else:
                    c += t[i]
            q.append(c)
        return ans