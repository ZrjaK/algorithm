# 题目：885.螺旋矩阵 III
# 难度：MEDIUM
# 最后提交：2022-04-17 08:17:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        k = 0
        r, c = rStart, cStart
        res = [[r,c]]
        while len(res) != rows * cols:
            if k % 4 == 0:
                for i in range(c+1,c+k//2+2):
                    if r >= 0 and r < rows and i >= 0 and i < cols:
                        res.append([r, i])
                c += k//2 + 1
            elif k % 4 == 1:
                for i in range(r+1,r+k//2+2):
                    if i >= 0 and i < rows and c >= 0 and c < cols:
                        res.append([i, c])
                r += k//2 + 1
            elif k % 4 == 2:
                for i in range(c-1,c-k//2-2,-1):
                    if r >= 0 and r < rows and i >= 0 and i < cols:
                        res.append([r, i])
                c -= k//2 + 1
            else:
                for i in range(r-1,r-k//2-2,-1):
                    if i >= 0 and i < rows and c >= 0 and c < cols:
                        res.append([i, c])
                r -= k//2 + 1
            k += 1
        return res