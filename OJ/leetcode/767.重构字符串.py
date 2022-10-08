# 题目：767.重构字符串
# 难度：MEDIUM
# 最后提交：2022-08-28 01:46:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        if max(c.values()) > (len(s)+1)//2:
            return ""
        pq = [[-i, a] for a, i in c.items()]
        heapify(pq)
        ans = ""
        while len(pq) > 1:
            t1 = heappop(pq)
            t2 = heappop(pq)
            ans += t1[1] + t2[1]
            t1[0] += 1
            t2[0] += 1
            if t2[0]:
                heappush(pq, t2)
            if t1[0]:
                heappush(pq, t1)
        if pq:
            ans += pq[0][1]
        return ans