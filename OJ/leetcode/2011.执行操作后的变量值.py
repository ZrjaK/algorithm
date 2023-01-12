# 题目：2011.执行操作后的变量值
# 难度：EASY
# 最后提交：2022-12-23 02:55:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for i in operations:
            if "+" in i:
                ans += 1
            if "-" in i:
                ans -= 1
        return ans