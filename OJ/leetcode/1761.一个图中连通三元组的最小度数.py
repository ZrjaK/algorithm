# 题目：1761.一个图中连通三元组的最小度数
# 难度：HARD
# 最后提交：2022-09-14 16:10:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(set)
        for i, j in edges:
            d[i].add(j)
            d[j].add(i)
        ans = 1e99
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j+1, n+1):
                    if i in d[j] and j in d[k] and k in d[i]:
                        ans = min(ans, len(d[i])+len(d[j])+len(d[k])-6)
        return ans if ans < 1e90 else -1