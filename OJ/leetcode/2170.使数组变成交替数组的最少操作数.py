# 题目：2170.使数组变成交替数组的最少操作数
# 难度：MEDIUM
# 最后提交：2022-09-09 17:56:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c1 = Counter(nums[::2])
        c2 = Counter(nums[1::2])
        a = [(0, 0)] + sorted([(i, j) for i, j in c1.items()], key=lambda x:x[1])
        b = [(0, 0)] + sorted([(i, j) for i, j in c2.items()], key=lambda x:x[1])
        if a[-1][0] == b[-1][0]:
            if a[-1][1] + b[-2][1] > a[-2][1] + b[-1][1]:
                b.pop()
            else:
                a.pop()
        return len(nums) - a[-1][1] - b[-1][1]