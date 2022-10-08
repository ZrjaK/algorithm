# 题目：1502.判断能否形成等差数列
# 难度：EASY
# 最后提交：2021-10-19 23:25:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(0, len(arr)-2):
            if arr[i+1] - arr[i] != arr[i+2] - arr[i+1]:
                return False
        return True