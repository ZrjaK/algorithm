# 题目：1385.两个数组间的距离值
# 难度：EASY
# 最后提交：2022-06-17 02:06:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for i in arr1:
            t = bisect.bisect_left(arr2, i)
            if t == len(arr2) or abs(i - arr2[t]) > d:
                if t == 0 or abs(i - arr2[t - 1]) > d:
                    ans += 1
        return ans
