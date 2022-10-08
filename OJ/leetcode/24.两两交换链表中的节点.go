// 题目：24.两两交换链表中的节点
// 难度：MEDIUM
// 最后提交：2022-03-20 22:29:10 +0800 CST
// 语言：golang
// 作者：ZrjaK

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    next := head.Next
    head.Next = swapPairs(next.Next)
    next.Next = head
    return next
}