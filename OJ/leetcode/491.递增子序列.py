# 题目：491.递增子序列
# 难度：MEDIUM
# 最后提交：2022-08-25 17:15:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(1<<n):
            if i.bit_count() < 2:
                continue
            t = []
            for j in range(n):
                if i & 1<<j:
                    t.append(nums[j])
            if sorted(t) == t:
                ans.add(tuple(t))
        return [list(i) for i in ans]