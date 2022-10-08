# 题目：2242.节点序列的最大得分
# 难度：HARD
# 最后提交：2022-09-28 08:59:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for i, j in edges:
            heappush(d[i], [-scores[j], j])
            heappush(d[j], [-scores[i], i])
        ans = -1
        for i, j in edges:
            for _, k in d[i][:5]:
                for _, l in d[j][:5]:
                    if len(set([i, j, k, l])) == 4:
                        ans = max(ans, sum(scores[t] for t in [i, j, k, l]))
        return ans