package main

import (
	"fmt"
	"strings"
)

var x []string

func main() {
	times := 0
	fmt.Scanf("%d\n", &times)
	x = make([]string, times)
	for i := 0; i < times; i++ {
		fmt.Scanf("%v", &x[i])
		fmt.Scanln()
	}
	for i := 0; i < times; i++ {
		fmt.Println(solution(x[i]))
	}
}

func solution(s string) string {
	i := 0
	for strings.Contains(s[i+1:], s[i:i+1]) {
		i++
	}
	return s[i:]
}
