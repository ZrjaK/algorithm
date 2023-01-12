# 题目：2509.查询树中环的长度
# 难度：HARD
# 最后提交：2022-12-18 16:42:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        for i, j in queries:
            if i > j:
                j, i = i, j
            c1 = c2 = 0
            while j.bit_length() > i.bit_length():
                j >>= 1
                c2 += 1
            while i != j:
                c1 += 1
                c2 += 1
                i >>= 1
                j >>= 1
            ans.append(c1 + c2 + 1)
        return ans
