# 题目：720.词典中最长的单词
# 难度：MEDIUM
# 最后提交：2021-10-23 21:42:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words.sort(key=len, reverse=True)
        
        words_set = set(words)
        
        for w in words:
            flag = False
            for i in range(1, len(w)+1):
                if w[:i] not in words_set:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                return w
        return ''