# 题目：2453.摧毁一系列目标
# 难度：MEDIUM
# 最后提交：2022-10-29 22:50:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        d = defaultdict(list)
        for i in nums:
            d[i%space].append(i)
        
        ans = 0
        ma = 0
        f = max(len(i) for i in d.values())
        h = []
        for i in d:
            if len(d[i]) == f:
                for j in d[i]:
                    h.append(j)
        return sorted(h)[0]