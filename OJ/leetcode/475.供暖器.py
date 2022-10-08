# 题目：475.供暖器
# 难度：MEDIUM
# 最后提交：2022-04-23 16:38:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = -1e99
        for i in houses:
            j = bisect_left(heaters, i)
            right = heaters[j] - i if j < len(heaters) else 1e99
            left = i - heaters[j-1] if j-1 >= 0 else 1e99
            ans = max(ans, min(right, left))
        return ans