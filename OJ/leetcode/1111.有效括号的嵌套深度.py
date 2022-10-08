# 题目：1111.有效括号的嵌套深度
# 难度：MEDIUM
# 最后提交：2022-09-03 14:36:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        n = len(seq)
        stackA = []
        stackB = []
        ans = [0] * n
        for i, v in enumerate(seq):
            if v == ")":
                if len(stackA) > len(stackB):
                    stackA.pop()
                    ans[i] = 0
                else:
                    stackB.pop()
                    ans[i] = 1
            else:
                if len(stackA) < len(stackB):
                    stackA.append("(")
                    ans[i] = 0
                else:
                    stackB.append("(")
                    ans[i] = 1
        return ans