# 题目：2569.更新数组后处理求和查询
# 难度：HARD
# 最后提交：2023-02-19 00:09:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        x = 0
        for i in range(n):
            if nums1[i]:
                x |= 1 << i
        ans = sum(nums2)
        out = []
        for op, l, r in queries:
            if op == 1:
                x ^= ((1 << r + 1) - 1) - ((1 << l) - 1)
            if op == 2:
                ans += x.bit_count() * l
            if op == 3:
                out.append(ans)
        return out
        