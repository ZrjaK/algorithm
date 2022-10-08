# 题目：810.黑板异或游戏
# 难度：HARD
# 最后提交：2022-09-29 10:19:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return reduce(xor, nums) == 0 if len(nums) % 2 else True