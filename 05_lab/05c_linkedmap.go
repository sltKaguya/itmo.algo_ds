package main

import (
	"bufio"
	"math"
	"os"
	"strings"
)

type Node struct {
	index    int
	value    string
	next     *Node
	previous *Node
}

type LinkedList struct {
	first *Node
}

func (list *LinkedList) put(index int, value string) {
	elem := &Node{index: index, value: value}

	if list.get(index) == nil {
		if list.first != nil {
			list.first.previous = elem
		}
		elem.next = list.first
		list.first = elem
	} else {
		list.get(index).value = value
	}
}

func (list *LinkedList) delete(index int) {
	elem := list.get(index)

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

func (list *LinkedList) get(index int) *Node {
	elem := list.first

	for elem != nil {
		if elem.index == index {
			return elem
		} else {
			elem = elem.next
		}
	}
	return elem
}

func (list *LinkedList) prev(index int) *Node {
	elem := list.get(index)

	if elem != nil {
		return elem.previous
	}
	return elem
}

func (list *LinkedList) next(index int) *Node {
	elem := list.get(index)

	if elem != nil {
		return elem.next
	}
	return elem
}

func hash(key string, size int) int {
	hash_sum := 5381
	for _, elem := range key {
		hash_sum = ((hash_sum << 5) + hash_sum) + int(elem)
	}
	return hash_sum
}

func main() {
	f_in, _ := os.Open("linkedmap.in")
	scanner := bufio.NewScanner(f_in)
	scanner.Split(bufio.ScanLines)
	var results []string
	size := 100000
	hash_table := make([]LinkedList, size)

	for scanner.Scan() {
		command := strings.Fields(scanner.Text())
		index_hashed := hash(command[1], size)
		index := int(math.Abs(float64(index_hashed % size)))
		check := hash_table[index].get(index)

		switch command[0] {
		case "put":
			value := command[2]
			hash_table[index].put(index, value)

		case "delete":
			hash_table[index].delete(index)

		case "get":
			if check != nil {
				results = append(results, check.value)
			} else {
				results = append(results, "none")
			}

		case "prev":
			if hash_table[index].prev(index) != nil {
				results = append(results, check.previous.value)
			} else {
				results = append(results, "none")
			}

		case "next":
			if hash_table[index].prev(index) != nil {
				results = append(results, check.next.value)
			} else {
				results = append(results, "none")
			}
		}
	}
	f_out, _ := os.Create("linedmap.out")
	f_out.WriteString(strings.Join(results, "\n"))
	f_out.Close()
}
