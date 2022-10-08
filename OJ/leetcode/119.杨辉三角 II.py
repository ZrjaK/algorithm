# 题目：119.杨辉三角 II
# 难度：EASY
# 最后提交：2021-10-20 22:10:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex+1):
            now = [1]*(i+1)
            if i >= 2:
                for n in range(1,i):
                    now[n] = pre[n-1]+pre[n]
            result += [now]
            pre = now
        return result[-1]