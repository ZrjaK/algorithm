# 题目：1534.统计好三元组
# 难度：EASY
# 最后提交：2021-10-20 00:09:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count