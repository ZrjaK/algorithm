# 题目：744.寻找比目标字母大的最小字母
# 难度：EASY
# 最后提交：2021-10-24 11:06:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target < letters[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return letters[l % len(letters)]