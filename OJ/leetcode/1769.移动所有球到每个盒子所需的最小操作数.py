# 题目：1769.移动所有球到每个盒子所需的最小操作数
# 难度：MEDIUM
# 最后提交：2022-12-02 08:20:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        h = []
        for i in range(n):
            if boxes[i] == "1":
                h.append(i)
        ans = []
        for i in range(n):
            t = 0
            for j in h:
                t += abs(i-j)
            ans.append(t)
        return ans