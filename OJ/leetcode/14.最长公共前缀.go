// 题目：14.最长公共前缀
// 难度：EASY
// 最后提交：2022-03-18 19:12:31 +0800 CST
// 语言：golang
// 作者：ZrjaK

func longestCommonPrefix(strs []string) string {
    sort.Strings(strs)
    i := 0
    for i < len(strs[0]) && strs[0][i] == strs[len(strs)-1][i] {
        i++
    }
    return strs[0][:i]
}