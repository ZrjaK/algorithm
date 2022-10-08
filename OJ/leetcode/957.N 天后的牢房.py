# 题目：957.N 天后的牢房
# 难度：MEDIUM
# 最后提交：2022-08-25 22:56:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        n %= 14
        if not n:
            n = 14
        res = [0] * 8
        for _ in range(n):
            for i in range(1, 7):
                res[i] = cells[i-1] ^ cells[i+1] ^ 1
            cells = [j for j in res]
        return res