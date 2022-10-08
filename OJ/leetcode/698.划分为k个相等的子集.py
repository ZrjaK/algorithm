# 题目：698.划分为k个相等的子集
# 难度：MEDIUM
# 最后提交：2022-09-20 08:30:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        target = sum(nums) // k
        if target != sum(nums) / k:
            return False
        f = [[] for _ in range(k+1)]
        h = [0] * (1<<n)
        for i in range(1<<n):
            h[i] = sum([nums[j] for j in range(n) if i>>j & 1] + [0])
            if h[i] % target == 0:
                f[h[i]//target].append(i)
        @cache
        def p(state, rest):
            if rest == 0:
                return True
            for i in f[k-rest]:
                if state & i == state and p(i, rest-1):
                    return True
            return False
        return p(0, k)