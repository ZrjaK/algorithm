# 题目：1019.链表中的下一个更大节点
# 难度：MEDIUM
# 最后提交：2022-09-03 14:17:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                ans[stack.pop()] = arr[i]
            stack.append(i)
        return ans