# 题目：338.比特位计数
# 难度：EASY
# 最后提交：2021-10-21 17:58:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            i = str(bin(i))[2:]
            count = 0
            for j in i:
                if j == "1":
                    count += 1
            l.append(count)
        return l