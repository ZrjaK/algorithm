# 题目：1732.找到最高海拔
# 难度：EASY
# 最后提交：2022-11-19 10:38:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = 0
        ans = 0
        for i in gain:
            s += i
            ans = max(ans, s)
        return ans