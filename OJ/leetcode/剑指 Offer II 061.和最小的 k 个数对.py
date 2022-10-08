# 题目：剑指 Offer II 061.和最小的 k 个数对
# 难度：MEDIUM
# 最后提交：2022-10-08 12:02:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        while pq and len(ans) < k:
            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans