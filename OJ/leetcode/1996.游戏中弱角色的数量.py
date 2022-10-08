# 题目：1996.游戏中弱角色的数量
# 难度：MEDIUM
# 最后提交：2022-09-01 14:26:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        maxdef = 0
        ans = 0
        for _, defs in properties:
            if defs < maxdef:
                ans += 1
            else:
                maxdef = defs
        return ans