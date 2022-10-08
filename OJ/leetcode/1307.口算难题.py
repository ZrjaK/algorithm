# 题目：1307.口算难题
# 难度：HARD
# 最后提交：2022-09-26 20:55:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        n = len(words)
        c = [0] * 26
        nozero = set()
        if len(result) > 1:
            nozero.add(ord(result[0])-65)
        result = result[::-1]
        for i in range(len(result)):
            c[ord(result[i])-65] -= 10**i
        for s in words:
            if len(s) > 1:
                nozero.add(ord(s[0])-65)
            s = s[::-1]
            for i in range(len(s)):
                c[ord(s[i])-65] += 10**i
        c = [[c[i], i] for i in range(26) if c[i]]
        c.sort(key=lambda x:-abs(x[0]))
        def p(i, state, s):
            if i == len(c):
                return s == 0
            for j in range(10)[::-1]:
                if state>>j & 1:
                    continue
                if j * sum([c[k][0] for k in range(i, len(c)) if c[k][0] > 0]) + s < 0 or \
                    j * sum([c[k][0] for k in range(i, len(c)) if c[k][0] < 0]) + s > 0:
                    return False
                break
            for j in range(10)[::-1]:
                if state>>j & 1:
                    continue
                if j == 0 and c[i][1] in nozero:
                    continue
                if p(i+1, state|1<<j, s + c[i][0]*j):
                    return True
            return False
        return p(0, 0, 0)