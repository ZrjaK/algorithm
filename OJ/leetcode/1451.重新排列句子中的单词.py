# 题目：1451.重新排列句子中的单词
# 难度：MEDIUM
# 最后提交：2022-08-30 20:30:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def arrangeWords(self, text: str) -> str:
        l = text.split(" ")
        l.sort(key=lambda x:len(x))
        l[0] = l[0].title()
        return " ".join(l[:1] + [i.lower() for i in l[1:]])