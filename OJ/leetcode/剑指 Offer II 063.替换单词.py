# 题目：剑指 Offer II 063.替换单词
# 难度：MEDIUM
# 最后提交：2022-10-08 12:07:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        l = sentence.split(" ")
        for i in range(len(l)):
            for w in dictionary:
                if l[i].startswith(w):
                    l[i] = w
        return " ".join(l)