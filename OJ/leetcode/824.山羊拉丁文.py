# 题目：824.山羊拉丁文
# 难度：EASY
# 最后提交：2021-10-24 15:13:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        for i in range(len(sentence)):
            if sentence[i][0].lower() in ["a", "e", "i", "o", "u"]:
                sentence[i] += "ma"
            else:
                sentence[i] = sentence[i][1:] + sentence[i][:1] + "ma"
            sentence[i] += "a" * (i + 1)
        return " ".join(sentence)
