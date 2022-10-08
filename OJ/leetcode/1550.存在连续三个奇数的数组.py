# 题目：1550.存在连续三个奇数的数组
# 难度：EASY
# 最后提交：2021-10-20 00:33:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False