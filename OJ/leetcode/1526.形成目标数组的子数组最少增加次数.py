# 题目：1526.形成目标数组的子数组最少增加次数
# 难度：HARD
# 最后提交：2022-10-18 17:42:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        target = [0] + target
        for i in range(1, len(target)):
                ans += max(0, target[i] - target[i-1])
        return ans