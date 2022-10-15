# 题目：2003.每棵子树内缺失的最小基因值
# 难度：HARD
# 最后提交：2022-10-14 19:24:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(nums)
        d = defaultdict(list)
        for i in range(n):
            d[parents[i]].append(i)
        ans = [1] * n
        from sortedcontainers import SortedList
        def findMex(tree: SortedList) -> int:
            """二分搜索缺失的第一个正整数,lc1539. 第 k 个缺失的正整数"""
            left, right = 0, len(tree) - 1
            while left <= right:
                mid = (left + right) >> 1
                diff = tree[mid] - (mid + 1)
                if diff >= 1:
                    right = mid - 1
                else:
                    left = mid + 1
            return left + 1
        def dfs(i):
            s = SortedList([nums[i]])
            for j in d[i]:
                t = dfs(j)
                s, t = sorted((s, t), key=len, reverse=True)
                s += t
            ans[i] = findMex(s)
            return s
        dfs(0)
        return ans