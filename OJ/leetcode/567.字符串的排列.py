# 题目：567.字符串的排列
# 难度：MEDIUM
# 最后提交：2022-05-20 14:19:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        t = [0] * 26
        for i in s1:
            t[ord(i)-ord('a')] += 1
        d = [0] * 26
        for i in s2[:len(s1)]:
            d[ord(i)-ord('a')] += 1
        if d == t:
            return True
        for i in range(len(s2)-len(s1)):
            d[ord(s2[i+len(s1)])-ord('a')] += 1
            d[ord(s2[i])-ord('a')] -= 1
            if d == t:
                return True
        return False