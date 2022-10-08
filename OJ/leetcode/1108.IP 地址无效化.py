# 题目：1108.IP 地址无效化
# 难度：EASY
# 最后提交：2021-11-06 16:11:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")