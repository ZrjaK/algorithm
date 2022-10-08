# 题目：1207.独一无二的出现次数
# 难度：EASY
# 最后提交：2021-11-13 21:47:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len((Counter(arr).values())) ==  len(set(Counter(arr).values()))