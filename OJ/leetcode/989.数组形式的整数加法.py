# 题目：989.数组形式的整数加法
# 难度：EASY
# 最后提交：2021-11-03 13:21:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(map(int, str(int(''.join(map(str, num)))+k)))