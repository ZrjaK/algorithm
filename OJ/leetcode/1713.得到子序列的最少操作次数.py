# 题目：1713.得到子序列的最少操作次数
# 难度：HARD
# 最后提交：2022-09-30 08:27:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        d = {}
        for i in range(len(target)):
            d[target[i]] = i
        h = []
        for i in arr:
            if i in d:
                f = d[i]
                t = bisect_left(h, f)
                if t < len(h):
                    h[t] = f
                else:
                    h.append(f)
        print(d, h)
        return len(target) - len(h)