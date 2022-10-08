# 题目：911.在线选举
# 难度：MEDIUM
# 最后提交：2022-09-14 14:34:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.d = defaultdict(int)
        a = 0
        s = [0] * len(persons)
        for p, t in zip(persons, times):
            s[p] += 1
            if s[p] >= s[a]:
                a = p
            self.d[t] = a
        self.times = times

    def q(self, t: int) -> int:
        i = bisect_right(self.times, t)
        if i == 0:
            return 0
        return self.d[self.times[i-1]]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)