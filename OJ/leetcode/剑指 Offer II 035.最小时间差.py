# 题目：剑指 Offer II 035.最小时间差
# 难度：MEDIUM
# 最后提交：2022-10-06 02:27:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        ans = 1e99
        for i in range(len(timePoints)):
            t1 = [int(i) for i in timePoints[i].split(":")]
            t2 = [int(i) for i in timePoints[i-1].split(":")]
            f = abs(t1[0]*60+t1[1] - (t2[0]*60+t2[1]))
            ans = min(ans, min(1440-f,f))
        return ans