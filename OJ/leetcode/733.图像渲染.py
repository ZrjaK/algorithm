# 题目：733.图像渲染
# 难度：EASY
# 最后提交：2021-10-24 10:54:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(i, j, base, m, n):
            if 0 <= i < m and 0 <= j < n and image[i][j] == base:
                image[i][j] = newColor
                dfs(i + 1, j, base, m, n)
                dfs(i - 1, j, base, m, n)
                dfs(i, j + 1, base, m, n)
                dfs(i, j - 1, base, m, n)
        
        if image[sr][sc] != newColor:
            dfs(sr, sc, image[sr][sc], len(image), len(image[0]))
        return image