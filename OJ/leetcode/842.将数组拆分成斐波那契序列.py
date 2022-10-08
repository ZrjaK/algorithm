# 题目：842.将数组拆分成斐波那契序列
# 难度：MEDIUM
# 最后提交：2022-09-14 11:54:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        @cache
        def p(x, i, j):
            if j == n:
                return [True, [j]]
            for k in range(j+1, min(n+1, j+32)):
                if str(int(num[x:i])) == num[x:i] and str(int(num[i:j])) == num[i:j] and str(int(num[j:k])) == num[j:k] and int(num[x:i]) + int(num[i:j]) == int(num[j:k]):
                    res = p(i, j, k)
                    if res[0]:
                        return [True, [j]+res[1]]
            return [False, []]
        for i in range(1, min(n, 33)):
            for j in range(i+1, min(n, i+33)):
                res = p(0, i, j)
                if res[0]:
                    l = [0, i]+res[1]
                    ans = []
                    for i in range(1, len(l)):
                        t = int(num[l[i-1]:l[i]])
                        if 0 <= t < 1<<31:
                            ans.append(t)
                        else:
                            return []
                    return ans
        return []