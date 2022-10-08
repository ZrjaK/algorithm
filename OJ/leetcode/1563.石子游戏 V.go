// 题目：1563.石子游戏 V
// 难度：HARD
// 最后提交：2022-09-19 10:10:30 +0800 CST
// 语言：golang
// 作者：ZrjaK

func stoneGameV(stoneValue []int) int {
    n := len(stoneValue)
    h := make([]int, n)
    h[0] = stoneValue[0]
    for i := 1; i < n; i++ {
        h[i] = h[i-1] + stoneValue[i]
    }
    dp := make([][]int, n)
    for i := range dp {
        dp[i] = make([]int, n)
        for j := range dp[i] {
            dp[i][j] = -1
        }
    }
    return p(0, n-1, h, dp)
}

func p(l int, r int, h []int, dp [][]int) int {
    if dp[l][r] != -1 {
        return dp[l][r]
    }
    res := 0
    for i := l; i < r; i++ {
        s1 := h[i]
        if l > 0 {
            s1 -= h[l-1]
        }
        s2 := h[r] - h[i]
        if s1 > s2 {
            res = max(res, p(i+1, r, h, dp) + s2)
        } else if s1 < s2 {
            res = max(res, p(l, i, h, dp) + s1)
        } else {
            res = max(res, p(i+1, r, h, dp) + s2)
            res = max(res, p(l, i, h, dp) + s1)
        }
    }
    dp[l][r] = res
    return res
}

func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}