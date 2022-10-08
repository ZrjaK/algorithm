# 题目：1525.字符串的好分割数目
# 难度：MEDIUM
# 最后提交：2022-07-18 14:29:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSplits(self, s: str) -> int:
        s1 = deque([ord(s[0])-97])
        s2 = deque(ord(i)-97 for i in s[1:])
        t1 = [0] * 26
        t2 = [0] * 26
        for i in s1:
            t1[i] += 1
        for i in s2:
            t2[i] += 1
        ans = 1 if t1.count(0) == t2.count(0) else 0
        while len(s2) > 1:
            t = s2.popleft()
            t2[t] -= 1
            s1.append(t)
            t1[t] += 1
            ans += 1 if t1.count(0) == t2.count(0) else 0
        return ans