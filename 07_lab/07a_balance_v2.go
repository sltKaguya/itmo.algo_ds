package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

type Node struct {
	value  int
	height int
	left   *Node
	right  *Node
}

type BinTree struct {
	root *Node
}

func main() {
	f_in, _ := os.Open("balance.in")
	scanner := bufio.NewScanner(f_in)
	scanner.Split(bufio.ScanLines)
	scanner.Scan()
	n := scanner.Text()
	var tree [][]int

	for scanner.Scan() {
		var array []int
		command := strings.Fields(scanner.Text())
		value, _ := strconv.Atoi(command[0])
		left, _ := strconv.Atoi(command[1])
		right, _ := strconv.Atoi(command[2])
		array = append(array, value, left, right, 1, 0)
		tree = append(tree, array)
	}
}
