# 题目：1170.比较字符串最小字母出现频次
# 难度：MEDIUM
# 最后提交：2022-05-04 14:17:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        h = []
        for i in words:
            a = 0
            for j in range(97,97+26):
                a = i.count(chr(j))
                if a:
                    break
            h.append(a)
        h.sort()
        res = []
        for i in queries:
            a = 0
            for j in range(97,97+26):
                a = i.count(chr(j))
                if a:
                    break
            t = len(h) - bisect_right(h, a)
            res.append(t)
        return res