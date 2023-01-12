# 题目：1832.判断句子是否为全字母句
# 难度：EASY
# 最后提交：2022-12-13 01:03:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(list(sentence))) == 26