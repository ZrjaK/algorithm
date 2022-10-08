# 题目：401.二进制手表
# 难度：EASY
# 最后提交：2022-08-25 00:41:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(12):
            for j in range(60):
                if i.bit_count() + j.bit_count() == turnedOn:
                    ans.append(f"{i}:{j:02d}")
        return ans