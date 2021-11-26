package main

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
		elem = nil
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
