# 题目：2550.猴子碰撞的方法数
# 难度：MEDIUM
# 最后提交：2023-01-29 16:48:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def monkeyMove(self, n: int) -> int:
        return (pow(2, n, int(1e9+7)) - 2) % int(1e9+7)