# 题目：2182.构造限制重复的字符串
# 难度：MEDIUM
# 最后提交：2022-09-09 18:19:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq = [0] * 26
        for i in s:
            pq[ord(i)-97] += 1
        pq = [[-i, pq[i]] for i in range(26) if pq[i]]
        heapify(pq)
        ans = ""
        while pq:
            s, t = heappop(pq)
            if t <= repeatLimit:
                ans += chr(-s+97) * t
            else:
                ans += chr(-s+97) * repeatLimit
                t -= repeatLimit
                if pq:
                    s1, t1 = heappop(pq)
                    t1 -= 1
                    ans += chr(-s1+97)
                    if t:
                        heappush(pq, [s, t])
                    if t1:
                        heappush(pq, [s1, t1])
                else:
                    break
        return ans