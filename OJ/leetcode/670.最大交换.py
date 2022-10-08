# 题目：670.最大交换
# 难度：MEDIUM
# 最后提交：2022-09-13 00:12:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        for i in range(n):
            ma = str(max([0] + [int(j) for j in s[i+1:]]))
            # print(i, ma)
            for j in range(n-1, i, -1):
                if s[j] == ma and ma > s[i]:
                    s[i], s[j] = s[j], s[i]
                    return int("".join(s))
                    break
        return num