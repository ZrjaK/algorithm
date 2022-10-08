# 题目：646.最长数对链
# 难度：MEDIUM
# 最后提交：2022-09-03 01:48:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        res, t = 1, pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > t:
                res += 1
                t = pairs[i][1]
        return res