# 题目：LCP 51.烹饪料理
# 难度：EASY
# 最后提交：2022-04-16 16:00:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
        def p(index, rest, restma):
            if index == len(attribute):
                if rest <= 0:
                    return 0
                else:
                    return -1e99
            f = [i for i in restma]
            p1 = p(index+1,rest, f[:])
            p2 = -1e99
            for j in range(len(cookbooks[index])):
                if f[j] - cookbooks[index][j] < 0:
                    return p1
                f[j] -= cookbooks[index][j]
            p2 = p(index+1, rest-attribute[index][1], f[:]) + attribute[index][0]
            return max(p1, p2)
        return max(-1, p(0, limit, materials[:]))