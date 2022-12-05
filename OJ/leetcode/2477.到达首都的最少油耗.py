# 题目：2477.到达首都的最少油耗
# 难度：MEDIUM
# 最后提交：2022-11-20 12:08:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        d = defaultdict(list)
        for i, j in roads:
            d[i].append(j)
            d[j].append(i)
        ans = 0
        def p(i, fa):
            nonlocal ans
            res = 1
            for j in d[i]:
                if j == fa:
                    continue
                res += p(j, i)
            if fa != -1:
                ans += (res-1) // seats + 1
            return res
        p(0, -1)
        return ans
                
        