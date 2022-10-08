# 题目：1774.最接近目标价格的甜点成本
# 难度：MEDIUM
# 最后提交：2022-07-21 00:14:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = [i for i in baseCosts]
        @cache
        def p(v, cost):
            res.append(cost)
            if cost >= target:
                return
            v = list(v)
            for i in range(len(v)):
                if v[i] < 2:
                    v[i] += 1
                    p(tuple(v), cost+toppingCosts[i])
                    v[i] -= 1
        for i in baseCosts:
            p(tuple([0] * len(toppingCosts)), i)
        p.cache_clear()
        res.sort()
        res.sort(key=lambda x:abs(target-x))
        return res[0]