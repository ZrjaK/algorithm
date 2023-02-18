# 题目：2564.子字符串异或查询
# 难度：MEDIUM
# 最后提交：2023-02-12 10:43:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        need = [i ^ j for i, j in queries]
        d = defaultdict(list)
        for i in range(len(queries)):
            d[need[i]].append(i)
        ans = [[-1, -1] for _ in range(len(queries))]
        for i in range(len(s)):
            for j in range(i, i+30):
                t = int(s[i:j+1], 2)
                if t in d:
                    for x in d[t]:
                        if ans[x] == [-1, -1] or j - i < ans[x][1] - ans[x][0]:
                            ans[x] = [i, j]
        return ans