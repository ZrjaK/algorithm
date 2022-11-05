# 题目：384.打乱数组
# 难度：MEDIUM
# 最后提交：2022-11-03 17:42:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:

    def __init__(self, nums: List[int]):
        self.arr1 = nums


    def reset(self) -> List[int]:
        return self.arr1


    def shuffle(self) -> List[int]:
        shuffArr = self.arr1.copy()
        random.shuffle(shuffArr)
        return shuffArr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()