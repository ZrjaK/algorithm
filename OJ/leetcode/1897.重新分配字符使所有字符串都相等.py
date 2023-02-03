# 题目：1897.重新分配字符使所有字符串都相等
# 难度：EASY
# 最后提交：2023-01-24 18:46:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter()
        for i in words:
            for j in i:
                c[j] += 1
        n = len(words)
        return all(i % n == 0 for i in c.values())