# 题目：1078.Bigram 分词
# 难度：EASY
# 最后提交：2021-11-06 15:57:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        l = text.split(" ")
        res = []
        for i in range(len(l)-2):
            if l[i] == first and l[i+1] == second:
                res.append(l[i+2])
        return res