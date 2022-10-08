# 题目：2178.拆分成最多数目的正偶数之和
# 难度：MEDIUM
# 最后提交：2022-04-05 18:32:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        r = []
        s = 0
        for i in range(2, finalSum+1,2):
            if s + i > finalSum:
                break
            r.append(i)
            s += i
        if r:
            r[-1] += finalSum - s
        return r