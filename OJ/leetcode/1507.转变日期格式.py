# 题目：1507.转变日期格式
# 难度：EASY
# 最后提交：2021-10-19 23:37:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reformatDate(self, date: str) -> str:
        Day, Month, Year = date.split(" ")
        Day = Day[:-2]
        MM = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        Month = MM.index(Month) + 1
        if int(Day) < 10:
            Day = "0" + Day
        if int(Month) < 10:
            Month = "0" + str(Month)
        return "{}-{}-{}".format(Year, Month, Day)
