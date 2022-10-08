# 题目：852.山脉数组的峰顶索引
# 难度：MEDIUM
# 最后提交：2022-08-24 03:03:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l+r>>1
            if arr[mid] > arr[mid+1]:
                r = mid - 1
            else:
                l = mid + 1
        return l