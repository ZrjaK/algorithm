# 题目：13.罗马数字转整数
# 难度：EASY
# 最后提交：2021-10-20 13:30:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
        ans=0        
        for i in range(len(s)):            
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:                
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans