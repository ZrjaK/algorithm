# 题目：2333.最小差值平方和
# 难度：MEDIUM
# 最后提交：2022-07-10 11:52:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSumSquareDiff(self, a: List[int], nums2: List[int], k1: int, k2: int) -> int:
        ans, k = 0, k1 + k2
        for i in range(len(a)):
            a[i] = abs(a[i] - nums2[i])
            ans += a[i] * a[i]
        if sum(a) <= k:
            return 0  # 所有 a[i] 均可为 0
        a.sort(reverse=True)
        a.append(0)  # 哨兵
        for i, v in enumerate(a):
            ans -= v * v
            j = i + 1
            c = j * (v - a[j])
            if c < k:
                k -= c
                continue
            v -= k // j
            return ans + k % j * (v - 1) * (v - 1) + (j - k % j) * v * v