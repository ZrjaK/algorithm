# 题目：38.外观数列
# 难度：MEDIUM
# 最后提交：2022-10-02 09:27:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

h = ["1"]
for _ in range(30):
    f = ""
    s = h[-1]
    t = []
    for i in s:
        if not t:
            t.append(i)
            continue
        if i == t[-1]:
            t.append(i)
        else:
            f += str(len(t)) + t[-1]
            t = [i]
    f += str(len(t)) + t[-1]
    h.append(f)

class Solution:
    def countAndSay(self, n: int) -> str:
        return h[n-1]