# 题目：492.构造矩形
# 难度：EASY
# 最后提交：2021-10-22 13:17:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a = math.sqrt(area)
        if int(a) - a == 0:
            return [int(a), int(a)]
        for i in range(int(a), 0, -1):
            if area / i == area // i:
                return [area // i, i]