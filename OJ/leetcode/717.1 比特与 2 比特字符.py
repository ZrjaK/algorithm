# 题目：717.1 比特与 2 比特字符
# 难度：EASY
# 最后提交：2021-10-23 21:31:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        start = 0
        while start < len(bits) - 1:
            if bits[start] == 0:
                start += 1
            else:
                start += 2
        return start == len(bits) - 1