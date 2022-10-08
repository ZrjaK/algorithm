# 题目：1601.最多可达成的换楼请求数目
# 难度：HARD
# 最后提交：2022-09-19 16:23:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        for i in range(1<<len(requests)):
            if ans >= i.bit_count():
                continue
            delta = [0] * n
            for j in range(len(requests)):
                if i>>j & 1:
                    delta[requests[j][0]] -= 1
                    delta[requests[j][1]] += 1
            if all(x == 0 for x in delta):
                ans = max(ans, i.bit_count())
        return ans