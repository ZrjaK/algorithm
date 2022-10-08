# 题目：341.扁平化嵌套列表迭代器
# 难度：MEDIUM
# 最后提交：2022-08-18 21:37:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        def p(l):
            for i in l:
                if i.isInteger():
                    self.res.append(i.getInteger())
                else:
                    p(i.getList())
        p(nestedList)
        self.index = -1
        
    
    def next(self) -> int:
        self.index += 1
        return self.res[self.index]
    
    def hasNext(self) -> bool:
        return self.index < len(self.res)-1

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())