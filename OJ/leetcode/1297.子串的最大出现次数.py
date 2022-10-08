# 题目：1297.子串的最大出现次数
# 难度：MEDIUM
# 最后提交：2022-04-03 15:55:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l = [s[i:i+minSize] for i in range(len(s)+1-minSize)]
        c = Counter(l)
        for i, j in c.most_common():
            if len(set(list(i))) <= maxLetters:
                return j
        return 0