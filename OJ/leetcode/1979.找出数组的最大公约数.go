// 题目：1979.找出数组的最大公约数
// 难度：EASY
// 最后提交：2022-03-22 08:33:49 +0800 CST
// 语言：golang
// 作者：ZrjaK

func findGCD(nums []int) int {
    return Gcd(Max(nums...), Min(nums...))
}

func Gcd(a int, b int) int {
    mo := a % b
    for mo != 0 {
        b, mo = mo, b % mo
    }
    return b
}

func Max(arg ...int) int {
	if arg == nil {
		return 0
	}
	r := arg[0]
	for _, v := range arg {
		if v > r {
			r = v
		}
	}
	return r
}

func Min(arg ...int) int {
	if arg == nil {
		return 0
	}
	r := arg[0]
	for _, v := range arg {
		if v < r {
			r = v
		}
	}
	return r
}