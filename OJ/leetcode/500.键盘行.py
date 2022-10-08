# 题目：500.键盘行
# 难度：EASY
# 最后提交：2021-10-22 14:46:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx<=set1 or setx<=set2 or setx<=set3:
                res.append(i)
               
            
        return res
            