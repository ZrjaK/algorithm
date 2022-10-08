# 题目：1968.构造元素不等于两相邻元素平均值的数组
# 难度：MEDIUM
# 最后提交：2022-09-01 14:06:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        n = len(nums)
        a = nums[:n//2+1]
        b = nums[n//2+1:]
        res = []
        while a and b:
            res.append(a.pop())
            res.append(b.pop())
        res += a + b
        return res