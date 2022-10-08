# 题目：2139.得到目标值的最少行动次数
# 难度：MEDIUM
# 最后提交：2022-09-09 17:33:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target != 1:
            if not maxDoubles:
                ans += target - 1
                target = 1
                break
            if target % 2:
                target -= 1
            else:
                target >>= 1
                maxDoubles -= 1
            ans += 1
        return ans