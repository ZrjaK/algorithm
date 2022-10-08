# 题目：1346.检查整数及其两倍数是否存在
# 难度：EASY
# 最后提交：2022-06-15 23:27:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = set()
        for i in arr:
            if i in d:
                return True
            if i % 2 == 0:
                d.add(i // 2)
            d.add(i * 2)
        return False