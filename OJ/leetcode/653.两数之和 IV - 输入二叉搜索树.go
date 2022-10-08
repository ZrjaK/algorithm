// 题目：653.两数之和 IV - 输入二叉搜索树
// 难度：EASY
// 最后提交：2022-03-21 03:21:08 +0800 CST
// 语言：golang
// 作者：ZrjaK

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findTarget(root *TreeNode, k int) bool {
    m := map[int]struct{}{}
    process(root, m)
    for i, _ := range m {
        if _, ok := m[k-i];ok && i != k-i {
            return true
        }
    }
    return false
}

func process(node *TreeNode, m map[int]struct{}) {
    if node == nil {
        return
    }
    m[node.Val] = struct{}{}
    process(node.Left, m)
    process(node.Right, m)
}