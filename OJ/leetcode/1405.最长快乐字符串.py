# 题目：1405.最长快乐字符串
# 难度：MEDIUM
# 最后提交：2022-04-12 15:02:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = [[a, "a"], [b, "b"], [c, "c"]]
        ans = ""
        while 1:
            for i in sorted(h, reverse=True):
                if i[0] < 1:
                    return ans
                if len(ans) > 1 and ans[-2:] == i[1] * 2:
                    continue
                ans += i[1]
                i[0] -= 1
                break
        return ans