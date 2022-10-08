# 题目：777.在LR字符串中交换相邻字符
# 难度：MEDIUM
# 最后提交：2022-10-02 00:44:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # 去掉X,两个字符串应该相等
        s = start.replace('X','')
        if s != end.replace('X',''):
            return False

        # start中R的索引要小于等于end的
        # start中L的索引要大于等于end的
        d1 = [ind for ind,i in enumerate(start) if i !='X']
        d2 = [ind for ind,i in enumerate(end) if i !='X']


        for ind,char in enumerate(s):
            # R 则start大于end的都是False
            if char == 'R' and d1[ind] > d2[ind]:
                return False
            if char == 'L' and d1[ind] < d2[ind]:
                return False
        return True