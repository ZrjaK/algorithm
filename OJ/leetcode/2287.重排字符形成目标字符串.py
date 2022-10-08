# 题目：2287.重排字符形成目标字符串
# 难度：EASY
# 最后提交：2022-05-29 10:57:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        l = list(s)
        ans = 0
        while s:
            for i in target:
                if i in l:
                    l.pop(l.index(i))
                else:
                    return ans
            ans += 1
        return ans