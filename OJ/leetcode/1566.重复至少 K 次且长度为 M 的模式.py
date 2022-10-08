# 题目：1566.重复至少 K 次且长度为 M 的模式
# 难度：EASY
# 最后提交：2021-10-20 10:55:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)):
            if arr[i:i+m] * k == arr[i:i+m*k]:
                return True
        return False