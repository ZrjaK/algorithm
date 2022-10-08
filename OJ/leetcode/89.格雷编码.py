# 题目：89.格雷编码
# 难度：MEDIUM
# 最后提交：2022-08-24 17:00:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res = res + [j|1<<i for j in res][::-1]
        return res
