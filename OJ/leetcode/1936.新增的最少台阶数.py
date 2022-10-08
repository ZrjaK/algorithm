# 题目：1936.新增的最少台阶数
# 难度：MEDIUM
# 最后提交：2022-09-08 11:55:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans = 0
        rungs = [0] + rungs
        for i in range(1, len(rungs)):
            if rungs[i] - rungs[i-1] > dist:
                ans += (rungs[i] - rungs[i-1]) // dist - 1
                if (rungs[i] - rungs[i-1]) % dist:
                    ans += 1
        return ans