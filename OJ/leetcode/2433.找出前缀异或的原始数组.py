# 题目：2433.找出前缀异或的原始数组
# 难度：MEDIUM
# 最后提交：2022-10-09 10:36:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        s = ans[0]
        for i in pref[1:]:
            ans.append(s ^ i)
            s ^= ans[-1]
        return ans
        