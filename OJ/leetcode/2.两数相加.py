# 题目：2.两数相加
# 难度：MEDIUM
# 最后提交：2022-01-06 02:27:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        s1 = ""
        p2 = l2
        s2 = ""
        while(p1 != None):
            s1 = str(p1.val) + s1
            p1 = p1.next
        while(p2 != None):
            s2 = str(p2.val) + s2
            p2 = p2.next
        l = list(str(int(s1) + int(s2)))[::-1]
        res = ListNode()
        p = res
        for i in range(len(l)):
            p.val = int(l[i])
            if i != len(l) - 1:
                p.next = ListNode()
                p = p.next
        return res

        