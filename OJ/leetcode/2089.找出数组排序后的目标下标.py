# 题目：2089.找出数组排序后的目标下标
# 难度：EASY
# 最后提交：2023-02-01 22:01:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i in range(len(nums)) if nums[i] == target]