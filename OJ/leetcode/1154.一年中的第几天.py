# 题目：1154.一年中的第几天
# 难度：EASY
# 最后提交：2022-09-04 17:01:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

import time
class Solution:
    def dayOfYear(self, date: str) -> int:
        return time.strptime(date, "%Y-%m-%d")[-2]