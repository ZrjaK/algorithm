# 题目：1411.给 N x 3 网格图涂色的方案数
# 难度：HARD
# 最后提交：2022-10-27 12:08:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numOfWays(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i, c):#i为当前的行下标，c为上一层是哪种排列
            if i == n:#当已经铺满
                return 1
            elif i == 0:#特殊情况，第一层
                return 6 * (dfs(i + 1, 0) + dfs(i + 1, 1)) % mod
            else:
                if c == 0:#如果上层为ABC
                    return 2 * (dfs(i + 1, 0) + dfs(i + 1, 1)) % mod
                else:#如果上层为ABA
                    return (2 * dfs(i + 1, 0) + 3 * dfs(i + 1, 1)) % mod
        mod = 10 ** 9 + 7
        return dfs(0, 0)