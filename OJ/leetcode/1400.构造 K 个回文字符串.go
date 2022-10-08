// 题目：1400.构造 K 个回文字符串
// 难度：MEDIUM
// 最后提交：2022-03-25 19:59:57 +0800 CST
// 语言：golang
// 作者：ZrjaK

func canConstruct(s string, k int) bool {
    if len(s) < k {
        return false
    }
    if len(s) == k {
        return true
    }
    m := map[string]int{}
    arr := strings.Split(s, "")
    for _, a := range arr {
        if _, ok := m[a]; ok {
            m[a]++
        } else {
            m[a] = 1
        }
    }
    count := 0
    for _, v := range m {
        if v % 2 == 1{
            count++
        }
    }
    if count <= k {
        return true
    }
    return false
}