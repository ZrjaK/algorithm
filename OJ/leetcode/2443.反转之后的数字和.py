# 题目：2443.反转之后的数字和
# 难度：MEDIUM
# 最后提交：2022-10-16 12:10:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num+1):
            if i + int(str(i)[::-1]) == num:
                return True
        return False