# 题目：23.合并K个升序链表
# 难度：HARD
# 最后提交：2022-04-04 22:55:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda a, b: 0 # 只需要定义即可，返回值我们用不到
        
        if not lists: return None
        nodeheap = []
        for node in lists: # 将每个链表的第一个node全部丢入heap
            if node:
                heapq.heappush(nodeheap, (node.val, node))
        
        HEAD = ListNode()
        p = HEAD
        
        while nodeheap: # 每pop一个node，push它的下一个node
            val, node = heapq.heappop(nodeheap)
            p.next = ListNode(val, None)
            p = p.next
            if node.next:
                heapq.heappush(nodeheap, (node.next.val, node.next))

        return HEAD.next
