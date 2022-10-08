# 题目：1178.猜字谜
# 难度：HARD
# 最后提交：2022-09-26 14:33:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        d = defaultdict(int)
        for s in words:
            t = 0
            for i in s:
                t |= 1<<ord(i)-97
            d[t] += 1
        ans = []
        for s in puzzles:
            a = 0
            for mask in range(1<<7):
                if not mask&1:
                    continue
                t = 0
                for i in range(len(s)):
                    if mask>>i & 1:
                        t |= 1<<ord(s[i])-97
                a += d[t]
            ans.append(a)
        return ans