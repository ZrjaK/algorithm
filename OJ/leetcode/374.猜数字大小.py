# 题目：374.猜数字大小
# 难度：EASY
# 最后提交：2021-10-21 19:12:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        mid = left + (right - left) / 2
        while guess(mid):
            if guess(mid) == 1:
                left = mid
            if guess(mid) == -1:
                right = mid
            mid = left + (right - left) / 2
        return int(mid)
