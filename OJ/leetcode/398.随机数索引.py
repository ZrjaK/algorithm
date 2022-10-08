# 题目：398.随机数索引
# 难度：MEDIUM
# 最后提交：2022-04-25 06:15:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = res = 1
        for i, n in enumerate(self.nums):
            if n == target:
                if random.random() < 1.0/cnt:
                    res = i
                cnt += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)