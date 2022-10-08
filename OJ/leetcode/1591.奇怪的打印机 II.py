# 题目：1591.奇怪的打印机 II
# 难度：HARD
# 最后提交：2022-09-27 21:28:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        d = defaultdict(lambda :[1e99, -1e99, 1e99, -1e99])
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                d[c][0] = min(d[c][0], i)
                d[c][1] = max(d[c][1], i)
                d[c][2] = min(d[c][2], j)
                d[c][3] = max(d[c][3], j)
        degree = defaultdict(int)
        f = defaultdict(list)
        for c in d:
            for i in range(d[c][0], d[c][1]+1):
                for j in range(d[c][2], d[c][3]+1):
                    if targetGrid[i][j] != c:
                        degree[c] += 1
                        f[targetGrid[i][j]].append(c)
        lst = [c for c in d if not degree[c]]
        cnt = 0
        while lst:
            cnt += len(lst)
            nxt = []
            for c in lst:
                for j in f[c]:
                    degree[j] -= 1
                    if not degree[j]:
                        nxt.append(j)
            lst = nxt
        return cnt == len(d)