# 题目：1128.等价多米诺骨牌对的数量
# 难度：EASY
# 最后提交：2021-11-06 22:45:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(comb(i,2) for i in Counter(tuple(sorted(j)) for j in dominoes).values())