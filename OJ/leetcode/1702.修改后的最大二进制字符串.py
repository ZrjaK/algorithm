# 题目：1702.修改后的最大二进制字符串
# 难度：MEDIUM
# 最后提交：2022-09-07 13:05:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        result = ""
        index = 0
        while index < n and binary[index] == '1':
            index += 1
            result += '1'
        t = binary[index:].count('0')
        if t < 2:
            return binary
        else:
            return result + '1'*(t-1) + '0' + '1'*(n-index-t)