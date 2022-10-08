# 题目：2251.花期内花的数目
# 难度：HARD
# 最后提交：2022-04-24 12:19:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start = sorted(i[0] for i in flowers)
        end = sorted(i[1] for i in flowers)
        n = len(persons)
        res = []
        for i in range(n):
            res.append(bisect_right(start, persons[i]) - bisect_left(end, persons[i]))
        return res