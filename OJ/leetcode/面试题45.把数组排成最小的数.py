# 题目：面试题45.把数组排成最小的数
# 难度：MEDIUM
# 最后提交：2022-10-03 18:34:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(x+y) - int(y+x)
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(compare))
        return "".join(nums)