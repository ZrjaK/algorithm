# 题目：面试题 17.08.马戏团人塔
# 难度：MEDIUM
# 最后提交：2023-01-06 13:21:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        h = [[i, j] for i, j in zip(height, weight)]
        return self.maxEnvelopes(h)
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num
        
        return len(f)