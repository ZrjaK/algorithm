# 题目：220.存在重复元素 III
# 难度：HARD
# 最后提交：2022-05-19 21:24:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        h = [[v, i] for i, v in enumerate(nums)]
        h.sort(key=lambda x:x[0])
        p = [i[0] for i in h]
        for i in range(len(h)):
            b = bisect_left(p, h[i][0]-t)
            for j in range(b, i):
                if abs(h[j][1]-h[i][1]) <= k:
                    return True
        return False