# 题目：1093.大样本统计
# 难度：MEDIUM
# 最后提交：2022-06-10 15:26:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = 0
        while count[minimum] == 0:
            minimum += 1
        maximum = 255
        while count[maximum] == 0:
            maximum -= 1
        mean = sum([count[i] * i for i in range(256)]) / sum(count)
        l, r = 0, 255
        sl, sr = count[l], count[r]
        while l < r-1:
            if sl > sr:
                r -= 1
                sr += count[r]
            else:
                l += 1
                sl += count[l]
        while count[l] == 0:
            l -= 1
        while count[r] == 0:
            r += 1
        if sl == sr:
            median = (l+r) / 2
        elif sl < sr:
            median = r
        else:
            median = l
        mode = count.index(max(count))
        return [minimum, maximum, mean, median, mode]