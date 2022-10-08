# 题目：6.Z 字形变换
# 难度：MEDIUM
# 最后提交：2022-09-30 10:15:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)