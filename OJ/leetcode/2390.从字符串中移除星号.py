# 题目：2390.从字符串中移除星号
# 难度：MEDIUM
# 最后提交：2022-08-28 10:36:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i in s:
            if i == "*":
                ans.pop()
            else:
                ans.append(i)
        return "".join(ans)