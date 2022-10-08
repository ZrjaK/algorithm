# 题目：2224.转化时间需要的最少操作数
# 难度：EASY
# 最后提交：2022-04-03 10:45:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        t = current.split(":")
        h1, m1 = int(t[0]), int(t[1])
        t = correct.split(":")
        h2, m2 = int(t[0]), int(t[1])
        ans1 = h2-h1
        if m2 < m1:
            
            q1 = m2+60-m1
            ans1 += q1//15
            q1 %= 15
            ans1 += q1//5
            q1 %= 5
            ans1 += q1
            ans1 -=1
        else:
            q1 = m2-m1
            ans1 += q1//15
            q1 %= 15
            ans1 += q1//5
            q1 %= 5
            ans1 += q1
        return ans1