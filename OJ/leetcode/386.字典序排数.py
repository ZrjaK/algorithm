# 题目：386.字典序排数
# 难度：MEDIUM
# 最后提交：2022-04-15 02:42:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def p(k):
            if k > n:
                return
            res.append(k)
            k *= 10
            for i in range(10):
                p(k+i)
        for i in range(1,10):
            p(i)
        return res
            

            