# 题目：860.柠檬水找零
# 难度：EASY
# 最后提交：2021-10-25 15:43:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = [0, 0]
        for i in bills:
            if i == 5:
                money[0] += 1
                continue
            elif i == 10 and money[0] >= 1:
                money[0] -= 1
                money[1] += 1
                continue
            elif i == 20:
                if money[1] >= 1 and money[0] >= 1:
                    money[1] -= 1
                    money[0] -= 1
                    continue
                elif money[0] >=3:
                    money[0] -= 3
                    continue
                else:
                    return False
            else:
                return False

        return True
