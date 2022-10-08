# 题目：791.自定义字符串排序
# 难度：MEDIUM
# 最后提交：2022-08-30 01:48:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return "".join(sorted(list(s), key=lambda x: order.index(x) if x in order else 300))