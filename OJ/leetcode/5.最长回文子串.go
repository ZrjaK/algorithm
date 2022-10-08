// 题目：5.最长回文子串
// 难度：MEDIUM
// 最后提交：2022-03-16 04:31:03 +0800 CST
// 语言：golang
// 作者：ZrjaK

func longestPalindrome(s string) string {
    arr := strings.Split(s, "")
    for i := len(arr); i > 1; i-- {
        for j := 0; j <= len(arr) - i; j++ {
            if t := arr[j:j+i];isSym(t){
                return strings.Join(t, "")
            }
        }
    }
    return s[:1]
}

func isSym(arr []string) bool {
    left := 0
    right := len(arr) - 1
    for (left <= right){
        if arr[left] != arr[right]{
            return false
        }
        left++
        right--
    }
    return true
}