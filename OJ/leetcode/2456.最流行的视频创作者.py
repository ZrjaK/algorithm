# 题目：2456.最流行的视频创作者
# 难度：MEDIUM
# 最后提交：2022-10-30 11:17:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        n = len(creators)
        ans = []
        d = defaultdict(int)
        h = defaultdict(list)
        f = defaultdict(list)
        for i in range(n):
            d[creators[i]] += views[i]
            h[creators[i]].append(ids[i])
            f[creators[i], ids[i]] = views[i]
        t = max(d.values())
        for i in d:
            if t != d[i]:
                continue
            h[i].sort(key=lambda x:(-f[i, x], x))
            ans.append([i, h[i][0]])
        return ans