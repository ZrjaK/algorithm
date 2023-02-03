# 题目：面试题 16.10.生存人数
# 难度：MEDIUM
# 最后提交：2023-01-30 20:33:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        diff = [0] * (10001)
        for i in birth:
            diff[i] += 1
        for i in death:
            diff[i+1] -= 1
        diff = list(accumulate(diff))
        return diff.index(max(diff))