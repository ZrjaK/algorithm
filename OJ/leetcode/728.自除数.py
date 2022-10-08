# 题目：728.自除数
# 难度：EASY
# 最后提交：2021-10-24 10:37:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            if "0" in str(i):
                continue
            for j in range(len(str(i))):
                if i % int(str(i)[j:j+1]) != 0:
                    break
                if j == len(str(i)) - 1:
                    res.append(i)
        return res
