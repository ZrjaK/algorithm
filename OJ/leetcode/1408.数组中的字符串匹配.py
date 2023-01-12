# 题目：1408.数组中的字符串匹配
# 难度：EASY
# 最后提交：2023-01-06 10:02:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [i for i in words if any(i in j for j in words if i != j)]