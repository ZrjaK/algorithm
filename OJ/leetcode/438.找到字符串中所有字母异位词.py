# 题目：438.找到字符串中所有字母异位词
# 难度：MEDIUM
# 最后提交：2022-05-20 14:14:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        t = [0] * 26
        for i in p:
            t[ord(i)-ord('a')] += 1
        d = [0] * 26
        for i in s[:len(p)]:
            d[ord(i)-ord('a')] += 1
        res = []
        if d == t:
            res.append(0)
        for i in range(len(s)-len(p)):
            d[ord(s[i+len(p)])-ord('a')] += 1
            d[ord(s[i])-ord('a')] -= 1
            if d == t:
                res.append(i+1)
        return res