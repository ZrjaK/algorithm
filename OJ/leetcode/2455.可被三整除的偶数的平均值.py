# 题目：2455.可被三整除的偶数的平均值
# 难度：EASY
# 最后提交：2022-10-30 10:30:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = 0
        c = 0
        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                s += i
                c += 1
        if not c:
            return 0
        return s // c