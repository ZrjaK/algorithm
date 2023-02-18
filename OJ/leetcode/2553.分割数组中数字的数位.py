# 题目：2553.分割数组中数字的数位
# 难度：EASY
# 最后提交：2023-02-04 22:30:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            t = []
            while i:
                t.append(i % 10)
                i //= 10
            ans += t[::-1]
        return ans