# 题目：1175.质数排列
# 难度：EASY
# 最后提交：2021-11-07 21:33:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def getA(n):
            b,r=n,1
            while b>1:
                r*=b
                b-=1
            return r
        #厄拉多塞筛法
        l=[1]*(n+1)
        l[0:2]=[0,0]
        for i in range(2,len(l)):
            if l[i]==1:
                l[i**2::i]=[0]*len(l[i**2::i])
        num_fact=sum(l)
        return getA(num_fact)*getA(n-num_fact)%(10**9+7)