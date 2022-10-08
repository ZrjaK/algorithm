# 题目：899.有序队列
# 难度：HARD
# 最后提交：2022-09-19 11:14:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(list(s)))
        return sorted([s[i:] + s[:i] for i in range(len(s))])[0]