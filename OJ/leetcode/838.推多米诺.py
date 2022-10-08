# 题目：838.推多米诺
# 难度：MEDIUM
# 最后提交：2022-06-04 19:27:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        od = ""
        while dominoes != od:
            od = dominoes
            dominoes = dominoes.replace("R.L", "T")
            dominoes = dominoes.replace(".L", "LL")
            dominoes = dominoes.replace("R.", "RR")
            dominoes = dominoes.replace("T", "R.L")
        return dominoes