# 题目：299.猜数字游戏
# 难度：MEDIUM
# 最后提交：2022-03-25 07:18:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        diff = [0] * 10
        cntA = 0
        cntB = 0
        for s, g in zip(secret, guess):
            if s == g:
                cntA += 1
            else:
                if diff[ord(g)-ord('0')] > 0:
                    cntB += 1
                if diff[ord(s)-ord('0')] < 0:
                    cntB += 1
                diff[ord(g) - ord('0')] -= 1
                diff[ord(s) - ord('0')] += 1
        return f'{cntA}A{cntB}B'
