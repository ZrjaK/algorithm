# 题目：2125.银行中的激光束数量
# 难度：MEDIUM
# 最后提交：2022-04-08 11:42:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        a = []
        for i in bank:
            t = i.count("1")
            if t:
                a.append(t)
        ans = 0
        for i in range(1,len(a)):
            ans += a[i]*a[i-1]
        return ans