# 题目：1861.旋转盒子
# 难度：MEDIUM
# 最后提交：2022-06-18 20:27:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i in range(len(box)):
            base = len(box[0]) - 1
            while base >= 0 and box[i][base] != ".":
                base -= 1
            t = base - 1
            while t >= 0:
                if box[i][t] == "*":
                    base = t-1
                    while base >= 0 and box[i][base] != ".":
                        base -= 1
                    t = base-1
                    continue
                if box[i][t] == "#":
                    box[i][base], box[i][t] = box[i][t], box[i][base]
                    base -= 1
                t -= 1

        res = [[""] * len(box) for _ in range(len(box[0]))]
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = box[-j-1][i]
        return res