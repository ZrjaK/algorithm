# 题目：2155.分组得分最高的所有下标
# 难度：MEDIUM
# 最后提交：2022-04-21 11:45:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        n0 = [0] * (n+1)
        n1 = [0] * (n+1)
        for i in range(1,n+1):
            n0[i] = n0[i-1]
            n0[i] += 1 if nums[i-1]==0 else 0
        for i in range(n-1,-1,-1):
            n1[i] = n1[i+1]
            n1[i] += 1 if nums[i]==1 else 0
        d = {}
        ma = -1e99
        for i in range(n+1):
            s = n0[i] + n1[i]
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
            ma = max(ma, s)
        return d[ma]