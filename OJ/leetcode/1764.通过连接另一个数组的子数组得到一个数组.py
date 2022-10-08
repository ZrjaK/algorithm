# 题目：1764.通过连接另一个数组的子数组得到一个数组
# 难度：MEDIUM
# 最后提交：2022-08-22 02:03:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        j = 0
        n = len(nums)
        for i in groups:
            while j < n and nums[j:j+len(i)] != i:
                j += 1
            if j >= n:
                return False
            j += len(i)
        return True
        