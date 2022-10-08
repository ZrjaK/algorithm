# 题目：284.顶端迭代器
# 难度：MEDIUM
# 最后提交：2022-10-03 16:33:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.a = []
        while iterator.hasNext():
            self.a.append(iterator.next())
        self.a = self.a[::-1]        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.a[-1]

    def next(self):
        """
        :rtype: int
        """
        return self.a.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.a) != 0

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].