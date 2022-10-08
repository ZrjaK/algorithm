# 题目：1366.通过投票对团队排名
# 难度：MEDIUM
# 最后提交：2022-08-30 17:04:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        ranking = collections.defaultdict(lambda: [0] * n)
        for vote in votes:
            for i, vid in enumerate(vote):
                ranking[vid][i] += 1
        
        result = list(ranking.items())
        result.sort(key=lambda x: (x[1], -ord(x[0])), reverse=True)
        return "".join([vid for vid, rank in result])