# 题目：1442.形成两个异或相等数组的三元组数目
# 难度：MEDIUM
# 最后提交：2022-08-26 16:19:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        h = list(accumulate(arr, lambda x, y: x^y)) + [0]
        ans = 0
        for k in range(n):
            for i in range(k):
                if h[i-1] == h[k]:
                    ans += k-i
        return ans