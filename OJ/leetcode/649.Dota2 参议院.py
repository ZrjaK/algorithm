# 题目：649.Dota2 参议院
# 难度：MEDIUM
# 最后提交：2022-09-05 10:54:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r = deque()
        d = deque()
        for i in range(n):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)
        while r and d:
            a = r.popleft()
            b = d.popleft()
            if a < b:
                r.append(a + n)
            else:
                d.append(b + n)
        if r:
            return "Radiant"
        else:
            return "Dire"