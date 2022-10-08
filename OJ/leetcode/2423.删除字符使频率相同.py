# 题目：2423.删除字符使频率相同
# 难度：EASY
# 最后提交：2022-10-01 22:35:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            if len(set(list(Counter(word[:i] +word[i+1:]).values()))) == 1:
                return True
        return False