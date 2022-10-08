# 题目：215.数组中的第K个最大元素
# 难度：MEDIUM
# 最后提交：2022-09-07 15:18:24 +0800 CST
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