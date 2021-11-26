package main

import (
	"bufio"
	"os"
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

func main() {
	f_in, _ := os.Open("set.in")
	scanner := bufio.NewScanner(f_in)
	scanner.Split(bufio.ScanLines)
}
