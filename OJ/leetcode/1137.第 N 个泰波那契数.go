// 题目：1137.第 N 个泰波那契数
// 难度：EASY
// 最后提交：2022-03-16 10:16:15 +0800 CST
// 语言：golang
// 作者：ZrjaK

func tribonacci(n int) int {
    if n == 0 {
        return 0
    }
    if n == 1 {
        return 1
    }
    if n == 2 {
        return 1
    }
    dp := make([]int, n+1)
    for i := range dp {
        dp[i] = -1
    }
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i := 3;i <= n; i++ {
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    }
    return dp[n]
}