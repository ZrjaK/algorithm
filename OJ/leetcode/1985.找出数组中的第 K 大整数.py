# 题目：1985.找出数组中的第 K 大整数
# 难度：MEDIUM
# 最后提交：2022-09-01 14:07:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        pq = []
        for i in nums:
            heappush(pq, int(i))
            if len(pq) > k:
                heappop(pq)
        return str(pq[0])