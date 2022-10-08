# 题目：1467.两个盒子中球的颜色数相同的概率
# 难度：HARD
# 最后提交：2022-09-30 08:48:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        s = sum(balls)
        l = len(balls)
        @cache
        def dfs(i, c, t):
            if i == l:
                return int(t == 0 and c == s // 2) #选了1/2的球数量且颜色无变化
            res = dfs(i + 1, c, t + 1) + dfs(i + 1, c + balls[i], t - 1)#不选和全选组合数都为1，直接相加即可，需要更新颜色变化
            for j in range(1, balls[i]):#其他情况，颜色无变化
                res += dfs(i + 1, c + j, t) * comb(balls[i], j)
            return res
        res = dfs(0, 0, 0)
        return res / comb(s, s // 2)