# 题目：659.分割数组为连续子序列
# 难度：MEDIUM
# 最后提交：2022-09-05 11:08:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        c = Counter(nums)
        end = defaultdict(int)
        for i in nums:
            if not c[i]:
                continue
            c[i] -= 1
            if end[i-1]:
                end[i-1] -= 1
                end[i] += 1
            elif c[i+1] and c[i+2]:
                c[i+1] -= 1
                c[i+2] -= 1
                end[i+2] += 1
            else:
                return False
        return True