# 题目：241.为运算表达式设计优先级
# 难度：MEDIUM
# 最后提交：2022-07-08 15:09:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    @cache
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        ops = {'+':lambda x,y:x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y}
        for indx in range(1,len(input)-1):
            if input[indx] in ops.keys():
                
                for left in self.diffWaysToCompute(input[:indx]):
                    for right in self.diffWaysToCompute(input[indx+1:]):
                        res.append(ops[input[indx]](left,right))                      
        if not res:
            res.append(int(input))
        
        return res