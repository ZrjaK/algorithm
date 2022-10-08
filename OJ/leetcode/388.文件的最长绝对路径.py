# 题目：388.文件的最长绝对路径
# 难度：MEDIUM
# 最后提交：2022-09-02 12:27:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        s = input.split("\n")
        l = 0
        stack = []
        ans = 0
        for i in s:
            c = i.count("\t")
            while stack and stack[-1][1] >= c:
                t = stack.pop()
                l -= t[0]
            t = len(i) - c + int(bool(c))
            l += t
            stack.append((t, c, i))
            if "." in i:
                ans = max(ans, l)
                # print(stack)
        return ans