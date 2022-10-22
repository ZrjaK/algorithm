# 题目：2117.一个区间内所有数乘积的缩写
# 难度：HARD
# 最后提交：2022-10-19 12:17:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        res = list(str(reduce(mul, range(left, right+1))))
        c = 0
        while res[-1] == "0":
            res.pop()
            c += 1
        if len(res) > 10:
            return "".join(res[:5])+"..."+"".join(res[-5:])+"e"+str(c)
        else:
            return "".join(res)+"e"+str(c)