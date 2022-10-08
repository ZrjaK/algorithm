# 题目：1927.求和游戏
# 难度：MEDIUM
# 最后提交：2022-09-08 11:49:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sumGame(self, num: str) -> bool:
        a = num[:len(num)//2]
        b = num[len(num)//2:]
        sa = sb = wa = wb = 0
        for i in a:
            if i == "?":
                wa += 1
            else:
                sa += int(i)
        for i in b:
            if i == "?":
                wb += 1
            else:
                sb += int(i)
        if (wa + wb) % 2:
            return True
        return  sa - sb != (wb - wa) * 9 // 2