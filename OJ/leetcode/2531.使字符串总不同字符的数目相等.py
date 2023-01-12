# 题目：2531.使字符串总不同字符的数目相等
# 难度：MEDIUM
# 最后提交：2023-01-08 15:34:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter([ord(i)-97 for i in word1])
        c2 = Counter([ord(i)-97 for i in word2])
        for i in range(26):
            if c1[i] == 0:
                continue
            for j in range(26):
                if c2[j] == 0:
                    continue
                t1 = c1 - Counter([i]) + Counter([j])
                t2 = c2 + Counter([i]) - Counter([j])
                if len([k for k in t1.values() if k]) == len([k for k in t2.values() if k]):
                    return True
        return False