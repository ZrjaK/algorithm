# 题目：167.两数之和 II - 输入有序数组
# 难度：MEDIUM
# 最后提交：2021-10-20 22:50:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1      
        while left < right:
            if numbers[left] + numbers[right] == target:                
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                right = right - 1