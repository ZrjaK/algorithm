// 题目：606.根据二叉树创建字符串
// 难度：EASY
// 最后提交：2022-03-19 20:20:48 +0800 CST
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
func tree2str(root *TreeNode) string {
    res := process(root)
    return res[1:len(res)-1]
}

func process(curNode *TreeNode) string {
    if curNode == nil {
        return ""
    }
    res := "(" + strconv.Itoa(curNode.Val)
    if curNode.Left == nil && curNode.Right != nil {
        res += "()"
    }
    res += process(curNode.Left) + process(curNode.Right)
    res += ")"
    return res
}