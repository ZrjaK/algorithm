# 题目：LCP 30.魔塔游戏
# 难度：MEDIUM
# 最后提交：2023-01-30 09:04:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1
        ans = 0
        s = 1
        pq = []
        for i in nums:
            s += i
            heappush(pq, i)
            if s <= 0:
                s -= heappop(pq)
                ans += 1
        return ans