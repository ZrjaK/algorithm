# 题目：2007.从双倍数组中还原原数组
# 难度：MEDIUM
# 最后提交：2022-04-22 19:32:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        # 数组长度是奇数一定无解
        if (n & 1) == 1:
            return []
        changed.sort()

        res, q = [], collections.deque()
        # 排序后按顺序遍历，原值 x 与双倍值 y 一定
        # 按顺序排列在一起，且 x 一定都在其 y 的前面
        # 当遍历到原数组值的双倍，则将小的加入
        # 否则预存小值等待双倍出现
        for x in changed:
            if q and q[0] * 2 == x:
                res.append(q.popleft())
            else:
                q.append(x)
        
        # 最后若队列非空，表示有 x 找不到 y
        return [] if q else res