# 题目：1805.字符串中不同整数的数目
# 难度：EASY
# 最后提交：2022-05-13 23:11:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(map(int, re.findall('\d+', word))))