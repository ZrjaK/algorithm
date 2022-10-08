# 题目：140.单词拆分 II
# 难度：HARD
# 最后提交：2022-04-06 02:28:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)
        def f(r, sr):
            if not sr:
                res.append(r[1:])
            for i in range(1, len(sr)+1):
                k = sr[:i]
                if k in wordDict:
                    f(f'{r} {k}', sr[i:])
        f("", s)
        return res
