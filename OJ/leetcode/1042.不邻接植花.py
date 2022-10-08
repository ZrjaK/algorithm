# 题目：1042.不邻接植花
# 难度：MEDIUM
# 最后提交：2022-08-05 03:23:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i, j in paths:
            d[i].append(j)
            d[j].append(i)
        ans = [0] * (n+1)
        for i in range(1, n+1):
            if ans[i]:
                continue
            q = deque([i])
            while q:
                cur = q.popleft()
                ban = set()
                for nxt in d[cur]:
                    if not ans[nxt]:
                        q.append(nxt)
                    else:
                        ban.add(ans[nxt])
                for i in range(1, 5):
                    if i not in ban:
                        ans[cur] = i
                        break

        return ans[1:]