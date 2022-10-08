// 题目：2272.最大波动的子字符串
// 难度：HARD
// 最后提交：2022-05-15 17:30:16 +0800 CST
// 语言：golang
// 作者：ZrjaK

func largestVariance(s string) int {
    n := len(s)
    r := make([]int, 200)
    for i := 0; i < n; i++ {
        r[s[i]] = i
    }
    ans := 0
    for i := 'a'; i <= 'z'; i++ {
        for j := 'a'; j <= 'z'; j++ {
            if i == j { 
                continue
            }
            cnti, cntj := 0, 0
            for z := 0; z < n; z++ {
                if rune(s[z]) == i {
                    cnti++
                }
                if rune(s[z]) == j {
                    cntj++
                }
                if cnti > 0 && cntj > 0 {
                    ans = max(ans, cnti-cntj)
                }
                if cnti < cntj && r[j] > z {
                    cnti, cntj = 0, 0
                }
            }
        }
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}