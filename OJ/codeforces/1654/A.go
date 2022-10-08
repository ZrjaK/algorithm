package main

import (
	"fmt"
	"sort"
)

var x [][]int

func main() {
	times := 0
	fmt.Scanf("%d\n", &times)
	x = make([][]int, times)
	for i := 0; i < times; i++ {
		var l int
		fmt.Scanf("%d\n", &l)
		x[i] = make([]int, l)
		for j := 0; j < l; j++ {
			fmt.Scanf("%d", &x[i][j])
		}
		fmt.Scanln()
	}
	for i := 0; i < times; i++ {
		fmt.Println(solution(x[i]))
	}
}

func solution(nums []int) int {
	sort.Ints(nums)
	return nums[len(nums)-1] + nums[len(nums)-2]
}
