# 题目：1185.一周中的第几天
# 难度：EASY
# 最后提交：2021-11-13 21:29:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.date(year,month,day).strftime('%A')