# 题目：2216.美化数组的最少删除数
# 难度：MEDIUM
# 最后提交：2022-03-27 10:49:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        count = 0
        i = 0
        isfindou = True
        while i < len(nums)-1:
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                if isfindou:
                    if i % 2 == 0:
                        # nums.pop(i+1)
                        i += 1
                        isfindou = False
                else:
                    if i % 2 == 1:
                        i += 1
                        isfindou = True
                        
                count += 1
            i += 2
            
        if (len(nums) - count) % 2 == 1:
            count += 1
        return count