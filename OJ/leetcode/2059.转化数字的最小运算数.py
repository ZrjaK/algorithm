# 题目：2059.转化数字的最小运算数
# 难度：MEDIUM
# 最后提交：2022-08-13 00:43:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        n = len(nums)
        op1 = lambda x, y: x + y
        op2 = lambda x, y: x - y
        op3 = lambda x, y: x ^ y
        ops = [op1, op2, op3]   # 运算符列表
        vis = [False] * 1001   # 可操作范围内整数的访问情况
        q = deque([(start, 0)])
        vis[start] = True
        while q:
            x, step = q.popleft()
            # 枚举数组中的元素和操作符并计算新生成的数值
            for i in range(n):
                for op in ops:
                    nx = op(x, nums[i])
                    # 如果新生成的数值等于目标值，则返回对应操作数
                    if nx == goal:
                        return step + 1
                    # 如果新生成的数值位于可操作范围内且未被加入队列，则更改访问情况并加入队列
                    if 0 <= nx <= 1000 and vis[nx] is False:
                        vis[nx] = True
                        q.append((nx, step + 1))
        # 不存在从初始值到目标值的转化方案
        return -1