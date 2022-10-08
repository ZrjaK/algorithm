# 题目：1505.最多 K 次交换相邻数位后得到的最小整数
# 难度：HARD
# 最后提交：2022-09-28 22:03:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        from sortedcontainers import SortedList
        d = defaultdict(deque)
        for i in range(len(num)):
            d[num[i]].append(i)
        res = []
        sl = SortedList() 
        for j in range(len(num)):
            for a in '0123456789':
                if d[a]:
                    i = d[a][0]
                    dis = i + len(sl) - sl.bisect(i) - j
                    if dis <= k:
                        k -= dis
                        d[a].popleft()
                        res.append(a)
                        sl.add(i)
                        break
        return ''.join(res)