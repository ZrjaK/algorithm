# 题目：2322.从树中删除边的最小分数
# 难度：HARD
# 最后提交：2022-10-14 11:12:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)

        xor, in_, out, time = [0] * n, [0] * n, [0] * n, 0
        def dfs(i, fa) -> None:
            nonlocal time
            time += 1
            in_[i] = time
            xor[i] = nums[i]
            for j in d[i]:
                if j == fa:
                    continue
                dfs(j, i)
                xor[i] ^= xor[j]
            out[i] = time
        dfs(0, -1)

        ans = inf
        for i in range(2, n):
            for j in range(1, i):
                if in_[i] < in_[j] <= out[i]:  # i 是 j 的祖先节点
                    x, y, z = xor[j], xor[i] ^ xor[j], xor[0] ^ xor[i]
                elif in_[j] < in_[i] <= out[j]:  # j 是 i 的祖先节点
                    x, y, z = xor[i], xor[i] ^ xor[j], xor[0] ^ xor[j]
                else:  # 删除的两条边分别属于两颗不相交的子树
                    x, y, z = xor[i], xor[j], xor[0] ^ xor[i] ^ xor[j]
                ans = min(ans, max(x, y, z) - min(x, y, z))
                if ans == 0: return 0  # 提前退出
        return ans