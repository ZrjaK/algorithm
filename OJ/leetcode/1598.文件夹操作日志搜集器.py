# 题目：1598.文件夹操作日志搜集器
# 难度：EASY
# 最后提交：2022-09-09 00:09:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for i in logs:
            if i == "../":
                ans = max(0, ans-1)
            elif i != "./":
                ans += 1
        return ans