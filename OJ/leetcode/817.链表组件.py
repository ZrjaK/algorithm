# 题目：817.链表组件
# 难度：MEDIUM
# 最后提交：2022-10-12 08:49:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        c = 0
        while head:
            if head.val in s:
                s.remove(head.val)
                c += 1
            else:
                ans += 1 if c else 0
                c = 0
            head = head.next
        ans += 1 if c else 0
        return ans