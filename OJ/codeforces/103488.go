package main

import "fmt"

func main() {
	times := 0
	fmt.Scanf("%d\n", &times)
	test := [][]float32{}
	for i := 0; i < times; i++ {
		var n, m, k float32
		fmt.Scanf("%f %f %f\n", &n, &m, &k)
		test = append(test, []float32{n, m, k})
	}
	for _, t := range test {
		fmt.Println(solution(t[0], t[1], t[2]))
	}
}

func solution(n float32, m float32, k float32) float32 {
	return k / m * (n - 1)
}
