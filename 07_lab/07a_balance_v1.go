package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func height(array [][]int, index int, len int) int {
	var copy [][]int
	copy = array
	max_height := 0

	for i := index; i < len; i++ {
		if copy[i][1] != 0 {
			copy[copy[i][1]-1][3] += copy[i][3]
		}
		if copy[i][2] != 0 {
			copy[copy[i][1]-1][3] += copy[i][3]
		}
		if copy[i][3] > max_height {
			max_height = copy[i][3]
		}
	}
	return max_height
}

func main() {
	f_in, _ := os.Open("balance.in")
	scanner := bufio.NewScanner(f_in)
	scanner.Split(bufio.ScanLines)
	var tree [][]int
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	for scanner.Scan() {
		var array []int
		command := strings.Fields(scanner.Text())
		value, _ := strconv.Atoi(command[0])
		left, _ := strconv.Atoi(command[1])
		right, _ := strconv.Atoi(command[2])
		array = append(array, value, left, right, 1)
		tree = append(tree, array)
	}

	for i := 0; i < n; i++ {
		println(height(tree, i, n), "\n")
	}
}
