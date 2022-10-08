# 题目：316.去除重复字母
# 难度：MEDIUM
# 最后提交：2022-04-19 15:33:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        stack = []
        a = set()
        for i in s:
            if i not in a:
                while stack and stack[-1] > i and c[stack[-1]] > 0:
                    a.remove(stack.pop())
                stack.append(i)
                a.add(i)
            c[i] -= 1
        return "".join(stack)