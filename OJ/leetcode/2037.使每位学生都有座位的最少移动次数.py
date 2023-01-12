# 题目：2037.使每位学生都有座位的最少移动次数
# 难度：EASY
# 最后提交：2022-12-31 00:44:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(i-j) for i, j in zip(sorted(seats), sorted(students)))