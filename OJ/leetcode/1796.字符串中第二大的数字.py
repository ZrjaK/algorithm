# 题目：1796.字符串中第二大的数字
# 难度：EASY
# 最后提交：2022-12-03 10:56:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def secondHighest(self, s: str) -> int:
        v = set()
        for i in s:
            if i.isdigit():
                v.add(int(i))
        v = sorted(list(v))
        return v[-2] if len(v) > 1 else -1