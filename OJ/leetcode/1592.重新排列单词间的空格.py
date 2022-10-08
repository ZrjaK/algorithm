# 题目：1592.重新排列单词间的空格
# 难度：EASY
# 最后提交：2022-09-07 00:25:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reorderSpaces(self, text: str) -> str:
        i = text.count(" ")
        l = [i for i in text.split(" ") if i]
        if len(l) == 1:
            return l[0] + i * " "
        t = " " * (i // (len(l)-1))
        return t.join(l) + " " * (i % (len(l)-1))