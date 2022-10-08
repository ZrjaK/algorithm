# 题目：1209.删除字符串中的所有相邻重复项 II
# 难度：MEDIUM
# 最后提交：2022-09-04 18:06:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1] += 1
            else:
                stack.append([i, 1])
            if stack[-1][1] == k:
                stack.pop()
        ans = ""
        for i, j in stack:
            ans += i * j
        return ans