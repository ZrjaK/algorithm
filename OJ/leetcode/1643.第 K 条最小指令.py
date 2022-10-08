# 题目：1643.第 K 条最小指令
# 难度：HARD
# 最后提交：2022-09-17 14:44:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v, h = destination
        ans = list()
        for i in range(h + v):
            if h > 0:
                o = comb(h + v - 1, h - 1)
                if k > o:
                    ans.append("V")
                    v -= 1
                    k -= o
                else:
                    ans.append("H")
                    h -= 1
            else:
                ans.append("V")
                v -= 1
        return "".join(ans)