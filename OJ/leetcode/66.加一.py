# 题目：66.加一
# 难度：EASY
# 最后提交：2021-10-20 19:48:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        l1 = []
        for i in digits:
            num += str(i)
        num = str(int(num) + 1)
        for i in num:
            l1.append(int(i))
        return l1