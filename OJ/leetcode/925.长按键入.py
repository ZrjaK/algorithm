# 题目：925.长按键入
# 难度：EASY
# 最后提交：2021-11-02 19:03:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name = list(name)
        typed = list(typed)
        while name:
            c = name.pop()
            if not typed or typed.pop() != c:
                return False
            if not name or name[-1] != c:
                while typed and typed[-1] == c:
                    typed.pop()
        return not typed