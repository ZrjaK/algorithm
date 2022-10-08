# 题目：761.特殊的二进制序列
# 难度：HARD
# 最后提交：2022-09-27 21:59:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        cnt = left = 0
        subs = list()

        for i, ch in enumerate(s):
            if ch == "1":
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    subs.append("1" + self.makeLargestSpecial(s[left+1:i]) + "0")
                    left = i + 1
        
        subs.sort(reverse=True)
        return "".join(subs)