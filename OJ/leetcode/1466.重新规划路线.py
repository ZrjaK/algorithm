# 题目：1466.重新规划路线
# 难度：MEDIUM
# 最后提交：2022-08-11 07:59:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edge = [[] for _ in range(n)]
        for p, c in connections:
            edge[p].append((c, 1))
            edge[c].append((p, 0))
        quee = [0]
        vist = [False] * n
        vist[0] = True
        ans = 0
        while quee:
            i = quee.pop(0)
            for n, c in edge[i]:
                if not vist[n]:
                    vist[n] = True
                    ans += c
                    quee.append(n)
        return ans