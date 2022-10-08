# 题目：剑指 Offer II 076.数组中的第 k 大的数字
# 难度：MEDIUM
# 最后提交：2022-10-08 14:26:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = list(set(nums))
        pq = []
        for i in nums:
            heappush(pq, i)
            if len(pq) > k:
                heappop(pq)
        return pq[0]