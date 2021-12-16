package main

import (
	"bufio"
	"os"
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
	n, _ := scanner.Text()

	for scanner.Scan()
}
