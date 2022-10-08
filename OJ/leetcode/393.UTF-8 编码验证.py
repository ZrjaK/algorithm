# 题目：393.UTF-8 编码验证
# 难度：MEDIUM
# 最后提交：2022-08-25 02:03:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        m1 = 0b00000000
        m2 = 0b11000000
        m3 = 0b11100000
        m4 = 0b11110000
        res = True
        i = 0
        while i < n:
            if data[i] & m4 == m4:
                res &= i+3 < n and \
                    0b11110000 <= data[i] < 0b11111000 and \
                    0b10000000 <= data[i+1] < 0b11000000 and \
                    0b10000000 <= data[i+2] < 0b11000000 and \
                    0b10000000 <= data[i+3] < 0b11000000
                i += 4
            elif data[i] & m3 == m3:
                res &= i+2 < n and \
                    0b11100000 <= data[i] < 0b11110000 and \
                    0b10000000 <= data[i+1] < 0b11000000 and \
                    0b10000000 <= data[i+2] < 0b11000000
                i += 3
            elif data[i] & m2 == m2:
                res &= i+1 < n and \
                    0b11000000 <= data[i] < 0b11100000 and \
                    0b10000000 <= data[i+1] < 0b11000000
                i += 2
            else:
                res &= data[i] < 1<<7
                i += 1
            if not res:
                return res
        return res