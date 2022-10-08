# 题目：1081.不同字符的最小子序列
# 难度：MEDIUM
# 最后提交：2022-09-03 14:27:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        c = Counter(s)
        stack = []
        v = set()
        for i in s:
            if i not in v:
                while stack and stack[-1] > i and c[stack[-1]]:
                    v.remove(stack.pop())
                stack.append(i)
                v.add(i)
            c[i] -= 1
        return "".join(stack)