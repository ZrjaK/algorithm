# 题目：2101.引爆最多的炸弹
# 难度：MEDIUM
# 最后提交：2022-08-13 15:55:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        @cache
        def check(t, j):
            return (bombs[t][0]-bombs[j][0])**2 + (bombs[t][1]-bombs[j][1])**2 <= bombs[t][2]**2
        n = len(bombs)
        ans = 1
        for i in range(n):
            q = deque([i])
            v = set()
            while q:
                t = q.popleft()
                # if t in v:
                #     continue
                # v.add(t)
                for j in range(n):
                    if j not in v and check(t, j):
                        v.add(j)
                        q.append(j)
            ans = max(ans, len(v))
        check.cache_clear()
        return ans