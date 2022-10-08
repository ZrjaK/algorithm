# 题目：1528.重新排列字符串
# 难度：EASY
# 最后提交：2021-10-20 00:01:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newstr = ""
        for i in range(len(indices)):
            for j in indices:
                if i == j:
                    newstr += s[indices.index(j):indices.index(j)+1]
        return newstr
