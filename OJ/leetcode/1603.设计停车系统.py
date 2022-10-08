# 题目：1603.设计停车系统
# 难度：EASY
# 最后提交：2021-10-20 12:13:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.bignow = 0
        self.mediumnow = 0
        self.smallnow = 0

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.bignow < self.big:
            self.bignow += 1
            return True
        if carType == 2 and self.mediumnow < self.medium:
            self.mediumnow += 1
            return True
        if carType == 3 and self.smallnow < self.small:
            self.smallnow += 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)