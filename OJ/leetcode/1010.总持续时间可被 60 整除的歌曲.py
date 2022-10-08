# 题目：1010.总持续时间可被 60 整除的歌曲
# 难度：MEDIUM
# 最后提交：2022-04-13 06:42:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = [0] * 60
        ans = 0
        for i in time:
            m = i % 60
            if m != 0:
                ans += d[60-m]
            else:
                ans += d[m]
            d[m] += 1
        return ans