// 题目：424.替换后的最长重复字符
// 难度：MEDIUM
// 最后提交：2022-05-20 13:59:27 +0800 CST
// 语言：golang
// 作者：ZrjaK

func characterReplacement(s string, k int) int {
    cnt := [26]int{}
    maxCnt, left := 0, 0
    ans := 0
    for right, ch := range s {
        cnt[ch-'A']++
        maxCnt = max(maxCnt, cnt[ch-'A'])
        for right-left+1-maxCnt > k {
            cnt[s[left]-'A']--
            left++
        }
        ans = max(ans, right-left+1)
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}