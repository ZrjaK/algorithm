# 题目：2100.适合打劫银行的日子
# 难度：MEDIUM
# 最后提交：2022-07-23 20:44:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        down = [0] * n
        for i in range(1, n):
            if security[i-1] >= security[i]:
                down[i] = down[i-1] + 1
        up = [0] * n
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                up[i] = up[i+1] + 1
        ans = []
        for i in range(n):
            if down[i] >= time and up[i] >= time:
                ans.append(i)
        return ans