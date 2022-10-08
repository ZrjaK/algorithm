# 题目：884.两句话中的不常见单词
# 难度：EASY
# 最后提交：2021-11-01 22:03:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = s1.split(" ") + s2.split(" ")
        return [i for i in res if res.count(i) == 1]