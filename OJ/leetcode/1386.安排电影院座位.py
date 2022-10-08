# 题目：1386.安排电影院座位
# 难度：MEDIUM
# 最后提交：2022-08-26 13:05:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        m1 = 0b111100
        m2 = 0b11110000
        m3 = 0b1111000000
        d = defaultdict(int)
        for i, j in reservedSeats:
            if 2<=j<=9:
                d[i] |= 1<<j
        ans = (n-len(d.keys())) * 2
        for i in d.values():
            if not m1 & i or not m2 & i or not m3 & i:
                ans += 1
        return ans