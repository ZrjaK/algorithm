// 题目：22.括号生成
// 难度：MEDIUM
// 最后提交：2022-03-24 01:16:19 +0800 CST
// 语言：golang
// 作者：ZrjaK

var res = []string{}
func generateParenthesis(n int) []string {
    res = []string{}
    process("", n, n)
    return res
}

func process(s string, left int, right int) {
    if left == 0 && right == 0 {
        res = append(res, s)
        return
    }
    if left > right {
        return
    } else if left == right {
        process(s+"(", left-1, right)
        return
    } else {
        if left != 0 {
            process(s+"(", left-1, right)
        }
        process(s+")", left, right-1)
    }
}