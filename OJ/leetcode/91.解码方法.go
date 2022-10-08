// 题目：91.解码方法
// 难度：MEDIUM
// 最后提交：2022-03-22 20:19:20 +0800 CST
// 语言：golang
// 作者：ZrjaK

func numDecodings(s string) int {
    dp := map[string]int{}
    return process(s, dp)
}

func process(s string, dp map[string]int) int {
    if t, ok := dp[s]; ok {
        return t
    }
    if s == "" {
        dp[s] = 1
        return dp[s]
    }
    if s[0:1] == "0" {
        dp[s] = 0
        return dp[s]
    }
    if len(s) == 1 {
        dp[s] = 1
        return dp[s]
    }
    res := process(s[1:], dp)
    if t, _ := strconv.Atoi(s[0:2]); t <= 26 {
        res += process(s[2:], dp)
    }
    dp[s] = res
    return dp[s]
}