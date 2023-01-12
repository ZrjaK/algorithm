# 题目：2042.检查句子中的数字是否递增
# 难度：EASY
# 最后提交：2023-01-04 01:17:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        h = []
        for i in s.split(" "):
            if i.isdigit():
                h.append(int(i))
        return h == sorted(set(h))