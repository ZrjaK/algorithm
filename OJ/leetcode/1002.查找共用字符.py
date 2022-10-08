# 题目：1002.查找共用字符
# 难度：EASY
# 最后提交：2021-11-03 19:24:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=[]
        if not words:
            return res
        key=set(words[0])
        for k in key:
            minnum = min(a.count(k) for a in words)
            res += minnum*k
        return res