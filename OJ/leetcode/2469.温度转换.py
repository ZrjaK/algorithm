# 题目：2469.温度转换
# 难度：EASY
# 最后提交：2022-11-13 10:30:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius +273.15, celsius*1.8+32]