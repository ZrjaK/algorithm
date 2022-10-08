# 题目：2293.极大极小游戏
# 难度：EASY
# 最后提交：2022-06-05 10:33:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        h = [i for i in nums]
        while len(h) != 1:
            t = []
            for i in range(0, len(h), 2):
                if (i // 2) % 2 == 0:
                    t.append(min(h[i], h[i+1]))
                else:
                    t.append(max(h[i], h[i+1]))
            h = [i for i in t]
        return h[0]