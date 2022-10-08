# 题目：2343.裁剪数字后查询第 K 小的数字
# 难度：MEDIUM
# 最后提交：2022-07-17 10:47:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        d = defaultdict(list)
        maxtrim = max(i[1] for i in queries)
        for i in range(1, maxtrim+1):
            for j in range(len(nums)):
                d[i].append((nums[j][-i:], j))
            d[i].sort(key=lambda x:int(x[0]))
        # print(d)
        for i, j in queries:
            res.append(d[j][i-1][1])
        return res
        