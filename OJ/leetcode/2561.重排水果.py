# 题目：2561.重排水果
# 难度：HARD
# 最后提交：2023-02-05 11:05:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)
        d = defaultdict(int)
        for i in basket1:
            d[i] += 1
        for i in basket2:
            d[i] += 1
        if any(i % 2 == 1 for i in d.values()):
            return -1
        for i in d:
            d[i] //= 2
        pos1 = defaultdict(list)
        for i in range(n):
            pos1[basket1[i]].append(i)
        pos2 = defaultdict(list)
        for i in range(n):
            pos2[basket2[i]].append(i)
        out1 = []
        for i in pos1:
            if len(pos1[i]) > d[i]:
                out1 += [i] * (len(pos1[i]) - d[i])
        out2 = []
        for i in pos2:
            if len(pos2[i]) > d[i]:
                out2 += [i] * (len(pos2[i]) - d[i])
        out1.sort()
        out2.sort(reverse=True)
        ans = 0
        mn = min(basket1+basket2)
        for i, j in zip(out1, out2):
            ans += min(min(i, j), mn * 2)
        return ans