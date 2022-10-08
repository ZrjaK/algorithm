// 题目：509.斐波那契数
// 难度：EASY
// 最后提交：2022-03-20 01:10:55 +0800 CST
// 语言：golang
// 作者：ZrjaK

func fib(n int) int {
    if n == 0 {
        return 0
    }
    if n == 1 {
        return 1
    }
    base := [][]int{{1, 1}, {1, 0}}
    res := maxtrixPower(base, n-2)
    return res[0][0] + res[1][0]
}

func maxtrixPower(m [][]int, p int) [][]int {
    res := make([][]int, len(m))
    for i := range res {
        res[i] = make([]int, len(m[0]))
        res[i][i] = 1
    }
    tmp := m
    for ; p != 0; p >>= 1 {
        if (p & 1) != 0 {
            res = muliMatrix(res, tmp)
        }
        tmp = muliMatrix(tmp, tmp)
    }
    return res
}

func muliMatrix(m1 [][]int, m2 [][]int) [][]int{
    res := make([][]int, len(m1))
    for i := range res {
        res[i] = make([]int, len(m2[0]))
    }
    for i := 0; i < len(m1); i++ {
        for j := 0; j < len(m2[0]); j++ {
            for k := 0; k < len(m2); k++ {
                res[i][j] += m1[i][k] * m2[k][j]
            }
        }
    }
    return res
}