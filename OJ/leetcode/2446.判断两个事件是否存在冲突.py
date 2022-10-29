# 题目：2446.判断两个事件是否存在冲突
# 难度：EASY
# 最后提交：2022-10-23 10:34:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        h1 = event1[0].split(":")
        s1 = int(h1[0]) * 60 + int(h1[1])
        h1 = event1[1].split(":")
        s2 = int(h1[0]) * 60 + int(h1[1])
        h1 = event2[0].split(":")
        s3 = int(h1[0]) * 60 + int(h1[1])
        h1 = event2[1].split(":")
        s4 = int(h1[0]) * 60 + int(h1[1])
        if s1 < s4:
            return s2 >= s3
        elif s1 > s4:
            return s2 <= s3
        return True