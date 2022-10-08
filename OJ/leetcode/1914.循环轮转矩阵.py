# 题目：1914.循环轮转矩阵
# 难度：MEDIUM
# 最后提交：2022-09-13 08:14:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        nlayer = min(m // 2, n // 2)   # 层数
        # 从左上角起逆时针枚举每一层
        for layer in range(nlayer):
            r = []   # 每个元素的行下标
            c = []   # 每个元素的列下标
            val = []   # 每个元素的数值
            for i in range(layer, m - layer - 1):   # 左 
                r.append(i)
                c.append(layer)
                val.append(grid[i][layer])
            for j in range(layer, n - layer - 1):   # 下
                r.append(m - layer - 1)
                c.append(j)
                val.append(grid[m-layer-1][j])
            for i in range(m - layer - 1, layer, -1):   # 右
                r.append(i)
                c.append(n - layer - 1)
                val.append(grid[i][n-layer-1])
            for j in range(n - layer - 1, layer, -1):   # 上
                r.append(layer)
                c.append(j)
                val.append(grid[layer][j])
            total = len(val)   # 每一层的元素总数
            kk = k % total   # 等效轮转次数
            # 找到每个下标对应的轮转后的取值
            for i in range(total):
                idx = (i + total - kk) % total   # 轮转后取值对应的下标
                grid[r[i]][c[i]] = val[idx]
        return grid