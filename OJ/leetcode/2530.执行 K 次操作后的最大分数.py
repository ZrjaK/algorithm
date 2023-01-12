# 题目：2530.执行 K 次操作后的最大分数
# 难度：MEDIUM
# 最后提交：2023-01-08 15:36:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = [-i for i in nums]
        heapify(pq)
        ans = 0
        while pq and k:
            i = -heappop(pq)
            ans += i
            i = (i - 1) // 3 + 1
            heappush(pq, -i)
            k -= 1
        return ans