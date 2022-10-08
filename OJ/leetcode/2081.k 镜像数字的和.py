# 题目：2081.k 镜像数字的和
# 难度：HARD
# 最后提交：2022-09-25 10:23:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isPalindrome(x: int) -> bool:
            digit = list()
            while x:
                digit.append(x % k)
                x //= k
            return digit == digit[::-1]

        left, cnt, ans = 1, 0, 0
        while cnt < n:
            right = left * 10
            # op = 0 表示枚举奇数长度回文，op = 1 表示枚举偶数长度回文
            for op in [0, 1]:
                # 枚举 i'
                for i in range(left, right):
                    if cnt == n:
                        break
                    
                    combined = i
                    x = (i // 10 if op == 0 else i)
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if isPalindrome(combined):
                        cnt += 1
                        ans += combined
            left = right
        
        return ans