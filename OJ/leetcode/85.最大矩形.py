# 题目：85.最大矩形
# 难度：HARD
# 最后提交：2022-10-06 20:09:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n, heights, st, ans = len(heights), [0] + heights + [0], [], 0
        for i in range(n + 2):
            while st and heights[st[-1]] > heights[i]:
                ans = max(ans, heights[st.pop(-1)] * (i - st[-1] - 1))
            st.append(i)

        return ans
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        heights = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            ans = max(ans, self.largestRectangleArea(heights))
        return ans
