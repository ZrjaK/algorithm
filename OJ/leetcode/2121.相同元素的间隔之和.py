# 题目：2121.相同元素的间隔之和
# 难度：MEDIUM
# 最后提交：2023-01-04 21:38:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        pos = defaultdict(list)
        for i, v in enumerate(arr):
            pos[v].append(i)  # 记录相同元素的位置
        ans = [0] * len(arr)
        for p in pos.values():  # 遍历每个组
            ans[p[0]] = s = sum(i - p[0] for i in p)  # 该组第一个元素的间隔和
            n = len(p)
            for i in range(1, n):
                s += (2 * i - n) * (p[i] - p[i - 1])  # 计算该组下一个元素的间隔和（考虑变化量）
                ans[p[i]] = s
        return ans
