# 题目：面试题61.扑克牌中的顺子
# 难度：EASY
# 最后提交：2022-10-03 20:59:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        h = list(set([i for i in nums if i]))
        if min(h) + 4 >= max(h) and len(h) + nums.count(0) == 5:
            return True
        return False