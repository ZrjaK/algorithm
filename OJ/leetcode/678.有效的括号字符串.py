# 题目：678.有效的括号字符串
# 难度：MEDIUM
# 最后提交：2022-07-06 18:45:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def p(i, left, right):
            if right > left:
                return False
            if i == len(s):
                if left == right:
                    return True
                else:
                    return False
            res = False
            if s[i] == "(":
                res |= p(i+1, left+1, right)
            elif s[i] == ")":
                res |= p(i+1, left, right+1)
            else:
                res |= p(i+1, left, right) or p(i+1, left+1, right) or p(i+1, left, right+1)
            return res
        return p(0, 0, 0)
            