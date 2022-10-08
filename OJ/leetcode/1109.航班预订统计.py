# 题目：1109.航班预订统计
# 难度：MEDIUM
# 最后提交：2022-09-20 17:40:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for i, j, k in bookings:
            diff[i-1] += k
            if j < n:
                diff[j] -= k
        return list(accumulate(diff))