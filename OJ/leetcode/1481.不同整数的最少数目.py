# 题目：1481.不同整数的最少数目
# 难度：MEDIUM
# 最后提交：2022-08-30 20:56:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        l = sorted(c.keys(), key=lambda x:c[x])
        for i in range(len(l)):
            if k >= c[l[i]]:
                k -= c[l[i]]
            else:
                return len(l)-i
        return 0