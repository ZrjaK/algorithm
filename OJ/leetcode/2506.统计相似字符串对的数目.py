# 题目：2506.统计相似字符串对的数目
# 难度：EASY
# 最后提交：2022-12-18 16:09:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        n = len(words)
        return len([1 for i in range(n) for j in range(i+1, n) if set(words[i]) == set(words[j])])