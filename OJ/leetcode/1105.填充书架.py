# 题目：1105.填充书架
# 难度：MEDIUM
# 最后提交：2022-07-13 02:59:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        @cache
        def dp(i, h, w):
            if i == n:
                return h                 
            maxh = max(h, books[i][1])
            if books[i][0] <= w:
                ans = min(dp(i+1, maxh, w-books[i][0]), dp(i+1, books[i][1], shelf_width-books[i][0])+h)
            else:
                ans = dp(i+1, books[i][1], shelf_width-books[i][0]) + h
            return ans

        return dp(0, 0, shelf_width)