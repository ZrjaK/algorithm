# 题目：2211.统计道路上的碰撞次数
# 难度：MEDIUM
# 最后提交：2022-04-18 14:48:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countCollisions(self, d: str) -> int:
        ans = 0
        ans += d.count("RL") * 2
        d = d.replace("RL", "S").split("S")
        if len(d) == 1:
            return 0
        for i in d[1:-1]:
            ans += len(i)
        ans += d[0].count("R") + d[-1].count("L")
        return ans