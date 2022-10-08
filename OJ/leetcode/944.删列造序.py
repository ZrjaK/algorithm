# 题目：944.删列造序
# 难度：EASY
# 最后提交：2021-11-03 12:45:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return [sorted(i) != list(i) for i in zip(*strs)].count(True)