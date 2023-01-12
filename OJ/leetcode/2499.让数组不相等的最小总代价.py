# 题目：2499.让数组不相等的最小总代价
# 难度：HARD
# 最后提交：2022-12-11 02:23:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        tmp = Counter()
        cnt = 0
        for i, (x1, x2) in enumerate(zip(nums1, nums2)):
            if x1 == x2:
                cnt += 1
                ans += i
                tmp[x1] += 1
        to_find = 0
        for item in tmp:
            if 2 * tmp[item] > cnt:
                to_find = tmp[item] * 2 - cnt
                break
        for i, (x1, x2) in enumerate(zip(nums1, nums2)):
            if to_find and x1 != x2 and x1 != item and x2 != item:
                to_find -= 1
                ans += i
        return ans if to_find == 0 else -1
