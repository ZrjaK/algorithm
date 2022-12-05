# 题目：1742.盒子中小球的最大数量
# 难度：EASY
# 最后提交：2022-11-23 10:02:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            c = i
            t = 0
            while c:
                t += c % 10
                c //= 10
            d[t] += 1
        return max(d.values())