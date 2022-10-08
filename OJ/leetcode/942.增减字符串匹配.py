# 题目：942.增减字符串匹配
# 难度：EASY
# 最后提交：2021-11-03 12:11:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = [i for i in range(len(s) + 1)]
        for i in range(len(s)):
            if s[i] == "D":
                res.insert(i, res.pop())
        return res