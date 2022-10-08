// 题目：1723.完成所有工作的最短时间
// 难度：HARD
// 最后提交：2022-09-27 14:21:33 +0800 CST
// 语言：golang
// 作者：ZrjaK

func minimumTimeRequired(jobs []int, k int) int {
    n := len(jobs)
    m := 1 << n
    sum := make([]int, m)
    for i := 1; i < m; i++ {
        x := bits.TrailingZeros(uint(i))
        y := i ^ 1<<x
        sum[i] = sum[y] + jobs[x]
    }

    dp := make([][]int, k)
    for i := range dp {
        dp[i] = make([]int, m)
    }
    for i, s := range sum {
        dp[0][i] = s
    }

    for i := 1; i < k; i++ {
        for j := 0; j < (1 << n); j++ {
            minn := math.MaxInt64
            for x := j; x > 0; x = (x - 1) & j {
                minn = min(minn, max(dp[i-1][j-x], sum[x]))
            }
            dp[i][j] = minn
        }
    }
    return dp[k-1][(1<<n)-1]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}