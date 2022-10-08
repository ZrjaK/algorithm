# 题目：1766.互质树
# 难度：HARD
# 最后提交：2022-09-26 14:19:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        @cache
        def _gcd(x, y):
            return gcd(x, y)
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        ans = [-1] * len(nums)
        h = [[] for _ in range(51)]
        depth = [0] * len(nums)
        def p(i, father, dep):
            depth[i] = dep
            for k in range(1, 51):
                if h[k] and _gcd(nums[i], k) == 1:
                    if ans[i] == -1:
                        ans[i] = h[k][-1]
                    if depth[h[k][-1]] > depth[ans[i]]:
                        ans[i] = h[k][-1]
            h[nums[i]].append(i)
            for j in d[i]:
                if j == father:
                    continue
                p(j, i, dep+1)
            h[nums[i]].pop()
        p(0, -1, 0)
        return ans