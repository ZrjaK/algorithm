# 题目：1588.所有奇数长度子数组的和
# 难度：EASY
# 最后提交：2021-10-20 11:36:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)+1):
                    if len(arr[i:j]) % 2 == 1:
                        s += sum(arr[i:j])
        return s