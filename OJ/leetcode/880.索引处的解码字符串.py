# 题目：880.索引处的解码字符串
# 难度：MEDIUM
# 最后提交：2022-09-14 20:56:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        b = set(list("1234567890"))
        c = 0
        for i in s:
            if i in b:
                c *= int(i)
            else:
                c += 1
        for i in s[::-1]:
            k %= c
            if not k and i not in b:
                return i
            if i in b:
                c //= int(i)
            else:
                c -= 1        