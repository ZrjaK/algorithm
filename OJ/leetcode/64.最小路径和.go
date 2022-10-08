// 题目：64.最小路径和
// 难度：MEDIUM
// 最后提交：2022-03-18 23:09:15 +0800 CST
// 语言：golang
// 作者：ZrjaK

func minPathSum(grid [][]int) int {
    m := len(grid)
    n := len(grid[0])
    dp := make([]int,len(grid[0])+1)
    for i := 1; i < len(dp); i++ {
        dp[i] = grid[len(grid)-1][i-1]
    }
    for row := m; row > 0; row-- {
        for col := n; col > 0; col-- {
            if row == m && col == n {
                continue
            } else if row == m {
                dp[col] = dp[col+1]
            } else if col == n {

            } else {
                dp[col] = min(dp[col] , dp[col+1] )
            }
            dp[col] += grid[row-1][col-1]
        }
    }
    return dp[1]
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}