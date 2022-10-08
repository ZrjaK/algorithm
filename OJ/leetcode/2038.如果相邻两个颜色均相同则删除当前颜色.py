# 题目：2038.如果相邻两个颜色均相同则删除当前颜色
# 难度：MEDIUM
# 最后提交：2022-03-22 00:09:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count = 0
        for i in range(len(colors)):
            if colors[i:i+3] == "AAA":
                count += 1
            if colors[i:i+3] == "BBB":
                count -= 1
        return count > 0