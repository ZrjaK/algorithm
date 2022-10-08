# 题目：324.摆动排序 II
# 难度：MEDIUM
# 最后提交：2022-08-27 15:25:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = sorted(nums)
        x = (n + 1) // 2
        j, k = x - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = arr[j]
            if i + 1 < n:
                nums[i + 1] = arr[k]
            j -= 1
            k -= 1