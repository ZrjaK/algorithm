# 题目：1470.重新排列数组
# 难度：EASY
# 最后提交：2022-08-29 02:28:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        ans = []
        for i, j in zip(nums[:n//2], nums[n//2:]):
            ans.append(i)
            ans.append(j)
        return ans