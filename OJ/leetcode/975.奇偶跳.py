# 题目：975.奇偶跳
# 难度：HARD
# 最后提交：2022-09-17 14:15:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        from sortedcontainers import SortedList
        maxl = [-1] * n
        minl = [-1] * n
        d = defaultdict(list)
        s = SortedList()
        for i in range(n-1, -1, -1):
            t = s.bisect_left(arr[i])
            if t < len(s):
                maxl[i] = d[s[t]][-1]
            d[arr[i]].append(i)
            s.add(arr[i])
        d = defaultdict(list)
        s = SortedList()
        for i in range(n-1, -1, -1):
            t = s.bisect_right(arr[i])
            if t > 0:
                minl[i] = d[s[t-1]][-1]
            d[arr[i]].append(i)
            s.add(arr[i])
        @cache
        def p(i, isodd):
            if i == -1:
                return False
            if i == n-1:
                return True
            if isodd:
                return p(maxl[i], not isodd)
            else:
                return p(minl[i], not isodd)
        ans = 0
        for i in range(n):
            if p(i, True):
                ans += 1
        return ans