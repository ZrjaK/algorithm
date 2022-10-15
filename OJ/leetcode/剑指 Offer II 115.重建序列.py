# 题目：剑指 Offer II 115.重建序列
# 难度：MEDIUM
# 最后提交：2022-10-10 21:50:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        indeg = [0] * (n+1)
        d = defaultdict(list)
        for s in sequences:
            for i in range(1, len(s)):
                d[s[i-1]].append(s[i])
                indeg[s[i]] += 1
        q = deque([i for i in range(1, n+1) if not indeg[i]])
        v = set()
        ans = []
        while q:
            if len(q) > 1:
                return False
            t = q.popleft()
            ans.append(t)
            for nxt in d[t]:
                indeg[nxt] -= 1
                if not indeg[nxt]:
                    q.append(nxt)
        return ans == nums