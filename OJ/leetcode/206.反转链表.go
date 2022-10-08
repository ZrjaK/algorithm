// 题目：206.反转链表
// 难度：EASY
// 最后提交：2022-03-21 05:35:20 +0800 CST
// 语言：golang
// 作者：ZrjaK

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(pHead *ListNode) *ListNode {
    pHead, nextnode := nil, pHead
    for nextnode != nil {
        nextnode.Next, pHead, nextnode = pHead, nextnode, nextnode.Next
    }
    return pHead
}