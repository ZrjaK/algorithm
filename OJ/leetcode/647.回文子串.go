// 题目：647.回文子串
// 难度：MEDIUM
// 最后提交：2022-03-16 05:16:07 +0800 CST
// 语言：golang
// 作者：ZrjaK

func countSubstrings(s string) int {
    count := 0
    arr := strings.Split(s, "")
    for i := len(arr); i > 0; i-- {
        for j := 0; j <= len(arr) - i; j++ {
            if t := arr[j:j+i];isSym(t){
                count += 1
            }
        }
    }
    return count
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