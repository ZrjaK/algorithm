# 题目：1338.数组大小减半
# 难度：MEDIUM
# 最后提交：2022-08-30 15:30:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        h = []
        for i, j in Counter(arr).items():
            h.append((i, j))
        h.sort(key=lambda x:-x[1])
        s = 0
        for i in range(len(h)):
            s += h[i][1]
            if s >= n/2:
                return i+1
                break
        return i