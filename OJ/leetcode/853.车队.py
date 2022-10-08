# 题目：853.车队
# 难度：MEDIUM
# 最后提交：2022-08-29 14:47:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        h = sorted(zip(position, speed), reverse=True)
        ans = []
        for i, j in h:
            if not ans or (target-i) / j > ans[-1]:
                ans.append((target-i) / j)
        return len(ans)