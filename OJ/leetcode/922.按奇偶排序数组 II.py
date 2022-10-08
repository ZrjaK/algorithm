# 题目：922.按奇偶排序数组 II
# 难度：EASY
# 最后提交：2021-11-02 18:53:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ou = [i for i in nums if i % 2]
        ji = [i for i in nums if not i % 2]
        return [i for n in zip(ji, ou) for i in n]