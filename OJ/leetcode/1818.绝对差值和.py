# 题目：1818.绝对差值和
# 难度：MEDIUM
# 最后提交：2022-05-10 14:59:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        diffs = [abs(nums1[i]-nums2[i]) for i in range(len(nums1))]
        nums1.sort()
        max_delta = 0
        for i,n in enumerate(nums2):
            if max_delta >= diffs[i]: #key
                continue
            idx = bisect_left(nums1,n)
            if idx == len(nums1):
                diff = abs(n-nums1[idx-1])
            elif idx > 0:
                diff = min(abs(n-nums1[idx-1]),abs(n-nums1[idx]))
            else:
                diff = abs(n-nums1[idx])
            max_delta = max(max_delta,diffs[i]-diff)
        return (sum(diffs) - max_delta) % 1000000007