# 题目：1433.检查一个字符串是否可以打破另一个字符串
# 难度：MEDIUM
# 最后提交：2022-08-30 20:26:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def p(s1, s2):
            d = [0] * 26
            for i in s2:
                d[ord(i)-97] += 1
            for i in s1:
                for j in range(26):
                    if d[j] and j >= ord(i)-97:
                        d[j] -= 1
                        break
                else: 
                    return False
            return True
        return p(s1, s2) or p(s2, s1)