# 题目：2451.差值数组不同的字符串
# 难度：EASY
# 最后提交：2022-10-29 22:32:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def oddString(self, words: List[str]) -> str:
        h = []
        for w in words:
            t = []
            for j in range(1, len(w)):
                t.append(ord(w[j])-ord(w[j-1]))
            h.append(t)
        for i in range(1, len(h)):
            if h[i] != h[i-1]:
                if h[i-1] != h[i-2]:
                    return words[i-1]
                else:
                    return words[i]