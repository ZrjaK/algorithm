# 题目：1552.两球之间的磁力
# 难度：MEDIUM
# 最后提交：2022-05-07 09:41:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 1, position[-1] - position[0]
        while l <= r:
            mid = l+r>>1
            c = t = 0
            while t < len(position):
                t = bisect_left(position, position[t] + mid)
                c += 1
            if c >= m:
                l = mid + 1
            else:
                r = mid - 1
        return r
