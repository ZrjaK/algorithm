# 题目：455.分发饼干
# 难度：EASY
# 最后提交：2021-10-22 12:11:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        for i in g:
            for j in s:
                if i <= j:
                    s.remove(j)
                    count += 1
                    break
        return count