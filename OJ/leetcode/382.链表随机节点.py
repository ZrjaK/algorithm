# 题目：382.链表随机节点
# 难度：MEDIUM
# 最后提交：2022-09-03 01:57:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.h = []
        while head:
            self.h.append(head.val)
            head =  head.next

    def getRandom(self) -> int:
        return choice(self.h)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()