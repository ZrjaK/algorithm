# 题目：834.树中距离之和
# 难度：HARD
# 最后提交：2022-09-23 09:25:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        dist = [0] * n
        cnt = [1] * n
        def p1(i, parent):
            for j in d[i]:
                if j == parent:
                    continue
                p1(j, i)
                cnt[i] += cnt[j]
                dist[i] += dist[j]
            dist[i] += cnt[i] - 1
        def p2(i, parent):
            for j in d[i]:
                if j == parent:
                    continue
                dist[j] = dist[i] - cnt[j] + n - cnt[j]
                p2(j, i)
        p1(0, -1)
        p2(0, -1)
        return dist