# 题目：2410.运动员和训练师的最大匹配数
# 难度：MEDIUM
# 最后提交：2022-09-17 22:42:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        ans = 0
        while players and trainers:
            if players[-1] <= trainers[-1]:
                ans += 1
                players.pop()
                trainers.pop()
            else:
                trainers.pop()
        return ans