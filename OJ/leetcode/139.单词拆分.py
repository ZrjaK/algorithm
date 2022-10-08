# 题目：139.单词拆分
# 难度：MEDIUM
# 最后提交：2022-04-06 02:23:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        
        @lru_cache(None)
        def process(st):
            if st == "":
                return True
            res = False
            for i in range(1,len(st)+1):
                if st[:i] in wordDict:
                    res = res or process(st[i:])
            return res
        return process(s)