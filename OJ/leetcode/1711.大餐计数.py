# 题目：1711.大餐计数
# 难度：MEDIUM
# 最后提交：2022-05-09 15:44:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        d = defaultdict(int)
        for i in deliciousness:
            d[i] += 1
        ans = 0
        for i, j in d.items():
            for k in range(22):
                t = 2**k - i
                # print(i, j, t)
                if t == i:
                    ans += (j-1) * j // 2
                elif t in d and t > i:
                    ans += j * d[t]
        return ans % int(1e9+7)