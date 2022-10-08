# 题目：2129.将标题首字母大写
# 难度：EASY
# 最后提交：2022-04-08 11:50:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l = title.title().split(" ")
        for i in range(len(l)):
            if len(l[i]) <= 2:
                l[i] = l[i].lower()
        return " ".join(l)