package main

import (
	"bufio"
	"math"
	"os"
	"strings"
)

type Node struct {
	index      int
	value      string
	next       *Node
	previous   *Node
	next_queue *Node
	prev_queue *Node
}

type LinkedList struct {
	first *Node
}

func (list *LinkedList) put(index int, value string, prev_queue *Node) *Node {
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
	elem.prev_queue = prev_queue
	if prev_queue != nil {
		prev_queue.next_queue = elem
	}
	return elem
}

func (list *LinkedList) delete(index int, prev_queue *Node) *Node {
	elem := list.get(index)
	ret_node := prev_queue

	if elem != nil {
		if elem.next != nil {
			elem.next.previous = elem.previous
		}
		if elem.previous != nil {
			elem.previous.next = elem.next
		} else {
			list.first = elem.next
		}
		if elem.prev_queue != nil {
			elem.prev_queue.next_queue = elem.next_queue
		}
		if elem.next_queue != nil {
			elem.next_queue.prev_queue = elem.prev_queue
		} else {
			ret_node = elem
		}
	}
	return ret_node
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

func (list *LinkedList) prev_q(index int) string {
	elem := list.get(index)

	if elem != nil {
		if elem.prev_queue != nil {
			return elem.prev_queue.value
		}
	}
	return "none"
}

func (list *LinkedList) next_q(index int) string {
	elem := list.get(index)

	if elem != nil {
		if elem.next_queue != nil {
			return elem.next_queue.value
		}
	}
	return "none"
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
	var in_queue *Node = nil

	for scanner.Scan() {
		command := strings.Fields(scanner.Text())
		index_hashed := hash(command[1], size)
		index := int(math.Abs(float64(index_hashed % size)))
		check := hash_table[index].get(index_hashed)
		switch command[0] {
		case "put":
			value := command[2]
			in_queue = hash_table[index].put(index_hashed, value, in_queue)

		case "delete":
			in_queue = hash_table[index].delete(index_hashed, in_queue)

		case "get":
			if check != nil {
				results = append(results, check.value)
			} else {
				results = append(results, "none")
			}

		case "prev":
			results = append(results, hash_table[index].prev_q(index_hashed))

		case "next":
			results = append(results, hash_table[index].next_q(index_hashed))
		}
	}
	f_out, _ := os.Create("linkedmap.out")
	f_out.WriteString(strings.Join(results, "\n"))
	f_out.Close()
}
