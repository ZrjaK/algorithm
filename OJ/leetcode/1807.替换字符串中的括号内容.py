# 题目：1807.替换字符串中的括号内容
# 难度：MEDIUM
# 最后提交：2023-01-12 17:08:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {}
        for i, j in knowledge:
            d[i] = j
        ans = []
        t = []
        f = 0
        for i in s:
            if i == "(":
                f = 1
                continue
            if i == ")":
                k = "".join(t)
                if k in d:
                    ans.append(d[k])
                else:
                    ans.append("?")
                t = []
                f = 0
                continue
            if f:
                t.append(i)
            else:
                ans.append(i)
        return "".join(ans)