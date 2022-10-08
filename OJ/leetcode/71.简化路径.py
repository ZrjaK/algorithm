# 题目：71.简化路径
# 难度：MEDIUM
# 最后提交：2022-04-12 18:47:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        for i in path.split("/"):
            if i not in {"", ".", ".."}:
                s.append(i)
            elif i == ".." and s:
                s.pop()
        return "/" + "/".join(s)