# 题目：1031.两个非重叠子数组的最大和
# 难度：MEDIUM
# 最后提交：2022-05-22 22:44:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        ans = 0
        n = len(nums)
        h = list(accumulate(nums))
        for i in range(n-firstLen+1):
            l1 = h[i+firstLen-1] - h[i-1] if i > 0 else h[i+firstLen-1]
            l2 = 0
            for j in range(i-secondLen+1):
                l2 = max(l2, h[j+secondLen-1]-h[j-1] if j > 0 else h[j+secondLen-1])
            for j in range(i+firstLen, n-secondLen+1):
                l2 = max(l2, h[j+secondLen-1]-h[j-1])
            ans = max(ans, l1+l2)
        return ans