# 题目：90.子集 II
# 难度：MEDIUM
# 最后提交：2022-08-24 16:47:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(1<<n):
            t = []
            for j in range(n):
                if 1<<j & i:
                    t.append(nums[j])
            res.add(tuple(sorted(t)))
        return [list(i) for i in res]