# 题目：2420.找到所有好下标
# 难度：MEDIUM
# 最后提交：2022-09-25 11:08:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        h1 = [1] * n
        h2 = [1] * n
        h1[0] = 0
        h2[-1] = 0
        c = 1
        for i in range(2, n):
            if nums[i-2] >= nums[i-1]:
                c += 1
            else:
                c = 1
            h1[i] = c
        c = 1
        for i in range(n-3, -1, -1):
            if nums[i+1] <= nums[i+2]:
                c += 1
            else:
                c = 1
            h2[i] = c
        ans = []
        # print(h1)
        # print(h2)
        for i in range(n):
            if h1[i] >= k and h2[i] >= k:
                ans.append(i)
        return ans