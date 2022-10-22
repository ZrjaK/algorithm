# 题目：1900.最佳运动员的比拼回合
# 难度：HARD
# 最后提交：2022-10-17 20:30:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dfs(players):
            n = len(players)
            pairs = [(players[i], players[~i]) for i in range((n + 1) // 2)]
            if (firstPlayer, secondPlayer) in pairs:
                return [1, 1]

            res = [1e99, -1e99]

            # 每组选1个，笛卡尔积
            for winners in product(*pairs):
                if firstPlayer not in winners or secondPlayer not in winners:
                    continue
                nexts = dfs(tuple(sorted(winners)))
                res = [min(res[0], 1 + nexts[0]), max(res[1], 1 + nexts[1])]
            return res

        return dfs(tuple(range(1, n + 1)))