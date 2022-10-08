// 题目：2207.字符串中最多数目的子字符串
// 难度：MEDIUM
// 最后提交：2022-03-19 23:11:25 +0800 CST
// 语言：golang
// 作者：ZrjaK

func maximumSubsequenceCount(text string, pattern string) int64 {
    s := strings.Split(text, "")
    p := strings.Split(pattern, "")
    
    dp := make([]int, len(s))
    t1 := 0
    for i := range dp {
        if s[i] == p[0] {
            t1++
        } else if s[i] == p[1] {
            dp[i] = t1
        }
    }
    t2 := 0
    for i := len(s) - 1; i >= 0;i-- {
        // if s[i] == p[0] {
        //     dp[i] = t2
        // }
        if s[i] == p[1] {
            t2++
        }
    }
    if p[0] == p[1] {
        return int64(t1 * (t1+1) / 2)
    }
    if t1 > t2 {
        return int64(sum(dp) + t1)
    }
    return int64(sum(dp) + t2)
}

func sum(nums []int) int {
    s := 0
    for _, v := range nums {
        s += v
    }
    return s
}