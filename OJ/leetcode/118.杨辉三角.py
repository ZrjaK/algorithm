# 题目：118.杨辉三角
# 难度：EASY
# 最后提交：2021-10-20 22:09:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            now = [1]*(i+1)
            if i >= 2:
                for n in range(1,i):
                    now[n] = pre[n-1]+pre[n]
            result += [now]
            pre = now
        return result