# 题目：1957.删除字符使字符串变好
# 难度：EASY
# 最后提交：2022-12-09 08:52:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        for i in s:
            if len(ans) > 1 and i == ans[-1] == ans[-2]:
                continue
            ans.append(i)
        return "".join(ans)