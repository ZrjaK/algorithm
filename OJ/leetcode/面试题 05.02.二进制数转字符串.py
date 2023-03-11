# 题目：面试题 05.02.二进制数转字符串
# 难度：MEDIUM
# 最后提交：2023-03-02 00:17:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def printBin(self, num: float) -> str:
        s = ["0."]
        for _ in range(6):  # 至多循环 6 次
            num *= 2
            if num < 1:
                s.append('0')
            else:
                s.append('1')
                num -= 1
                if num == 0:
                    return ''.join(s)
        return "ERROR"
