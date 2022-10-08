# 题目：2225.找出输掉零场或一场比赛的玩家
# 难度：MEDIUM
# 最后提交：2022-04-03 10:54:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        lose = {}
        for winner, loser in matches:
            win[winner] = 1
            if loser in lose.keys():
                lose[loser] += 1
            else:
                lose[loser] = 1
        for i in lose.keys():
            if i in win.keys():
                del win[i]
        ans = []
        r = []
        for i in win.keys():
            r.append(i)
        ans.append(sorted(r))
        r = []
        for i, j in lose.items():
            if j == 1:
                r.append(i)
        ans.append(sorted(r))
        return ans