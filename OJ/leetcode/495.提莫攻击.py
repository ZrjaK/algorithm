# 题目：495.提莫攻击
# 难度：EASY
# 最后提交：2021-10-22 13:36:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ret = 0
        pre = timeSeries[0]
        for i in range(len(timeSeries)):
            t = timeSeries[i] + duration 
            ret += min(t - pre,duration) 
            pre = t
        return ret