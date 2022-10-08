# 题目：1694.重新格式化电话号码
# 难度：EASY
# 最后提交：2022-10-01 01:40:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reformatNumber(self, number: str) -> str:
        h = []
        for i in number:
            if i.isdigit():
                if h and len(h[-1]) < 3:
                    h[-1] += i
                else:
                    h.append(i)
        if len(h[-1]) == 1:
            h[-2], h[-1] = h[-2][:-1], h[-2][-1] + h[-1]
        return "-".join(h)