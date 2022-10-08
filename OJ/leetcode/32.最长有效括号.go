// 题目：32.最长有效括号
// 难度：HARD
// 最后提交：2022-03-18 18:06:04 +0800 CST
// 语言：golang
// 作者：ZrjaK

func longestValidParentheses(s string) int {
    arr := strings.Split(s, "")
    dp := make([]int, len(s))
    for i := range dp {
        if arr[i] == ")" && i-1 >= 0 {
            pre := i - dp[i-1] - 1
            if pre >= 0 && arr[pre] == "(" {
                dp[i] = dp[i-1] + 2
                if pre != 0 {
                    dp[i] += dp[pre-1]
                }
            }
        }
    }
    return max(dp...)
}

func max(arg ...int) int {
    m := 0
    for _, v := range arg {
        if v > m {
            m = v
        }
    }
    return m
}