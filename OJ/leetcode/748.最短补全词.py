# 题目：748.最短补全词
# 难度：EASY
# 最后提交：2021-10-24 11:56:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

import re
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = re.sub("\d", "", licensePlate)
        licensePlate = re.sub("\s", "", licensePlate)
        licensePlate = sorted(licensePlate)
        minlen = 1001
        res = ""
        for i in words:
            word = i
            i = list(i.lower())
            for j in range(len(licensePlate)):
                if licensePlate[j].lower() in i:
                    i.remove(licensePlate[j].lower())
                else:
                    break
                if j == len(licensePlate) - 1:
                    if len(word) < minlen:
                        minlen = len(word)
                        res = word
        return res