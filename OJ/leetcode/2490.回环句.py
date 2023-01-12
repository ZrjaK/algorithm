# 题目：2490.回环句
# 难度：EASY
# 最后提交：2022-12-04 18:54:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        h = sentence.split(" ")
        if all(h[i][0] == h[i-1][-1] for i in range(len(h))):
            return True
        else:
            return False
            