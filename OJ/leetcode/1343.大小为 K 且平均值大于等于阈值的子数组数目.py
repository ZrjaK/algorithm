# 题目：1343.大小为 K 且平均值大于等于阈值的子数组数目
# 难度：MEDIUM
# 最后提交：2022-05-23 10:48:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = r = ans = s = 0
        while r < k:
            s += arr[r]
            r += 1
        ans += 1 if s >= k * threshold else 0
        while r < len(arr):
            s += arr[r]
            s -= arr[l]
            r += 1
            l += 1
            ans += 1 if s >= k * threshold else 0
        return ans