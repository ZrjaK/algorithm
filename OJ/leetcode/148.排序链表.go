// 题目：148.排序链表
// 难度：MEDIUM
// 最后提交：2022-06-02 20:05:32 +0800 CST
// 语言：golang
// 作者：ZrjaK

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func sortList(head *ListNode) *ListNode {
    return mergeSort(head)
}

func mergeSort(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    slow, fast := head, head.Next.Next
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }
    r := mergeSort(slow.Next)
    slow.Next = nil
    l := mergeSort(head)
    return merge(l, r)
}

func merge(l, r *ListNode) *ListNode {
    h := new(ListNode)
    p := h
    for l != nil && r != nil {
        if l.Val < r.Val {
            p.Next = l
            l = l.Next
        } else {
            p.Next = r
            r = r.Next
        }
        p = p.Next
    }
    if l != nil {
        p.Next = l
    } else {
        p.Next = r
    }
    return h.Next
}