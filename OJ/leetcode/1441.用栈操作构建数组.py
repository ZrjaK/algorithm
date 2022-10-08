# 题目：1441.用栈操作构建数组
# 难度：MEDIUM
# 最后提交：2022-09-04 23:04:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target = target[::-1]
        res = []
        for i in range(1, n+1):
            if not target:
                return res
            if i == target[-1]:
                res.append("Push")
                target.pop()
            else:
                res.append("Push")
                res.append("Pop")
        return res