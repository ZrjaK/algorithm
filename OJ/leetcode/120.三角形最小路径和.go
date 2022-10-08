// 题目：120.三角形最小路径和
// 难度：MEDIUM
// 最后提交：2022-03-24 02:24:25 +0800 CST
// 语言：golang
// 作者：ZrjaK

func minimumTotal(triangle [][]int) int {
    for i := len(triangle) - 2; i >= 0; i-- {
		for j := 0; j <= i; j++ {
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
		}
	}
	return triangle[0][0]
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}