# 题目：478.在圆内随机生成点
# 难度：MEDIUM
# 最后提交：2022-11-17 21:21:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        r = (random.random() ** 0.5) * self.radius
        theta = random.uniform(0, 2 * math.pi)
        return [r * math.cos(theta) + self.x, r * math.sin(theta) + self.y]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()