# 题目：1850.邻位交换的最小次数
# 难度：MEDIUM
# 最后提交：2022-06-14 20:41:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def gen(A):
            i = len(A)-2
            while A[i]>=A[i+1]:
                i -= 1
            j = len(A)-1
            while A[j]<=A[i]:
                j -= 1
            A[i], A[j] = A[j], A[i]
            return A[:i+1] + A[i+1:][::-1]
        T = list(num)
        for _ in range(k):
            T = gen(T)
        res = 0
        while T:
            pos = num.find(T[0])
            res += pos
            T, num = T[1:], num[:pos]+num[pos+1:]
        return res