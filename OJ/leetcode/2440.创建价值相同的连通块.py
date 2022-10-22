# 题目：2440.创建价值相同的连通块
# 难度：HARD
# 最后提交：2022-10-16 00:13:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        tot = sum(nums)
        possible_ans = []
        for i in range(len(nums), 0, -1):
            if tot % i == 0:
                possible_ans.append(i)
        d = defaultdict(list)
        for x, y in edges:
            d[x].append(y)
            d[y].append(x)

        for ans in possible_ans:
            target = tot // ans
            v = set()
            def check(node):
                v.add(node)
                res = nums[node]
                for nxt in d[node]:
                    if nxt in v:
                        continue
                    val = check(nxt)
                    if val < 0:
                        return -1
                    res += val
                return res % target if res <= target else -1
            if check(0) == 0:
                return ans - 1