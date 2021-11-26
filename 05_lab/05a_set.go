package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
	"strings"
)

type Node struct {
	value    int
	next     *Node
	previous *Node
}

type LinkedList struct {
	first *Node
}

func (list *LinkedList) insert(value int) {
	elem := &Node{value: value}

	if list.exists(value) == nil {
		if list.first != nil {
			list.first.previous = elem
		}
		elem.next = list.first
		list.first = elem
	}
}

func (list *LinkedList) exists(value int) *Node {
	elem := list.first

	for elem != nil {
		if elem.value == value {
			return elem
		} else {
			elem = elem.next
		}
	}
	return elem
}

func (list *LinkedList) delete(value int) {
	elem := list.exists(value)

	if elem != nil {
		if elem.next != nil {
			elem.next.previous = elem.previous
		}
		if elem.previous != nil {
			elem.previous.next = elem.next
		} else {
			list.first = elem.next
		}
	}
}

func main() {
	f_in, _ := os.Open("set.in")
	scanner := bufio.NewScanner(f_in)
	scanner.Split(bufio.ScanLines)
	var results []string
	size := 100000
	hash_table := make([]LinkedList, size)

	for scanner.Scan() {
		command := strings.Fields(scanner.Text())
		value, _ := strconv.Atoi(command[1])
		index := int(math.Abs(float64(value % size)))

		switch command[0] {
		case "insert":
			hash_table[index].insert(value)

		case "exists":
			if hash_table[index].exists(value) != nil {
				results = append(results, "true")
			} else {
				results = append(results, "false")
			}

		case "delete":
			hash_table[index].delete(value)
		}
	}
	f_out, _ := os.Create("set.out")
	f_out.WriteString(strings.Join(results, "\n"))
	f_out.Close()
}
