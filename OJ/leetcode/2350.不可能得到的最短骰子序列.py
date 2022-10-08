# 题目：2350.不可能得到的最短骰子序列
# 难度：HARD
# 最后提交：2022-07-24 08:52:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        res,cur=0,set()
        for i in rolls:
            if i not in cur:
                cur.add(i)
                if len(cur)==k:
                    res+=1
                    cur=set()
        return res+1