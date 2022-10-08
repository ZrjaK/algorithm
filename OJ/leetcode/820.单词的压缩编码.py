# 题目：820.单词的压缩编码
# 难度：MEDIUM
# 最后提交：2022-10-08 12:21:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return sum([len(w)+1 for w in s])