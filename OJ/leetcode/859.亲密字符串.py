# 题目：859.亲密字符串
# 难度：EASY
# 最后提交：2021-10-25 15:30:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        cnt = 0
        sa, sb = '', ''
        for i, j in zip(s, goal):
            if i != j:
                cnt += 1
                sa += i
                sb = j + sb
                if cnt == 3:
                    return False
        if (cnt == 2 and sa == sb) or (cnt==0 and len(set(s))!=len(s)):
            return True
        return False