# 题目：1094.拼车
# 难度：MEDIUM
# 最后提交：2022-08-30 04:03:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for i, j, k in trips:
            diff[j] += i
            diff[k] -= i
        m = 0
        for i in diff:
            m += i
            if m > capacity:
                return False
        return True