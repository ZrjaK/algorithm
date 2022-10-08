# 题目：636.函数的独占时间
# 难度：MEDIUM
# 最后提交：2022-09-02 13:46:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        time = 0
        for s in logs:
            i = s.split(":")
            t = [int(i[0]), i[1], int(i[2])]
            if stack and stack[-1][1] == "start":
                ans[stack[-1][0]] += t[2] - time
                time = t[2]
            if t[1] == "end":
                time += 1
                ans[stack[-1][0]] += 1
                stack.pop()
                continue
            stack.append(t)
        return ans