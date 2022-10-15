# 题目：面试题 01.01.判定字符是否唯一
# 难度：EASY
# 最后提交：2022-10-11 08:31:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)