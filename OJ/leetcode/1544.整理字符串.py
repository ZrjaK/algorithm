# 题目：1544.整理字符串
# 难度：EASY
# 最后提交：2022-09-01 19:36:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        for i in s:
            if ans and abs(ans[-1] - ord(i)) == 97-65:
                ans.pop()
            else:
                ans.append(ord(i))
        return "".join([chr(i) for i in ans])