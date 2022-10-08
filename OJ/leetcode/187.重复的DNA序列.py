# 题目：187.重复的DNA序列
# 难度：MEDIUM
# 最后提交：2022-05-19 16:16:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = defaultdict(int)
        for i in range(len(s)-9):
            d[s[i:i+10]] += 1
        return [k for k, v in d.items() if v > 1]