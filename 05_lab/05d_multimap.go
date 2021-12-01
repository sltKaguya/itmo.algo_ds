package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

const size int = 1000

type Node struct {
	key      string
	values   []LinkedList
	next     *Node
	previous *Node
}

type LinkedList struct {
	first *Node
}

func (list *LinkedList) put_x(key_x string, ind_y int, val_y string) {
	elem_x := list.get(key_x)

	if elem_x == nil {
		elem := &Node{
			key:    key_x,
			values: make([]LinkedList, size),
			next:   list.first,
		}
		if list.first != nil {
			list.first.previous = elem
		}
		list.first = elem
		elem_x = elem
	}
	elem_x.values[ind_y].put_y(val_y)
}

func (list *LinkedList) put_y(val_y string) {
	search_val := list.get(val_y)

	if search_val == nil {
		elem := &Node{
			key:    val_y,
			values: nil,
			next:   list.first}
		if list.first != nil {
			list.first.previous = elem
		}
		list.first = elem
	}
}

func (list *LinkedList) delete_y(key_x string, ind_y int, val_y string) {
	elem_x := list.get(key_x)

	if elem_x != nil {
		search_val := elem_x.values[ind_y].get(val_y)
		if search_val != nil {
			if search_val.next != nil {
				search_val.next.previous = search_val.previous
			}
			if search_val.previous != nil {
				search_val.previous.next = search_val.next
			} else {
				elem_x.values[ind_y].first = search_val.next
			}
		}
	}
}

func (list *LinkedList) deleteall(key_x string) {
	elem_x := list.get(key_x)

	if elem_x != nil {
		if elem_x.next != nil {
			elem_x.next.previous = elem_x.previous
		}
		if elem_x.previous != nil {
			elem_x.previous.next = elem_x.next
		} else {
			list.first = elem_x.next
		}
	}
}

func (list *LinkedList) get(key_y string) *Node {
	elem := list.first

	for elem != nil {
		if elem.key == key_y {
			return elem
		} else {
			elem = elem.next
		}
	}
	return elem
}

func (list *LinkedList) get_ys(key_x string) []string {
	search_key := list.get(key_x)
	count := 0
	var answers []string
	answers = append(answers, "0")

	if search_key != nil {
		for _, elem := range search_key.values {
			elem_y := elem.first
			for elem_y != nil {
				count += 1
				answers[0] = fmt.Sprint(count)
				answers = append(answers, elem_y.key)
				elem_y = elem_y.next
			}
		}
	}
	answers = append(answers, "\n")
	return answers
}

func hash(key string, size int) int {
	hash_sum := 5381
	for _, elem := range key {
		hash_sum = ((hash_sum << 5) + hash_sum) + int(elem)
	}
	return int(math.Abs(float64(hash_sum % size)))
}

func main() {
	f_in, _ := os.Open("multimap.in")
	f_out, _ := os.Create("multimap.out")
	scanner := bufio.NewScanner(f_in)
	scanner.Split(bufio.ScanLines)
	hash_table := make([]LinkedList, size)

	for scanner.Scan() {
		command := strings.Fields(scanner.Text())
		key_x := command[1]
		index_x := hash(key_x, size)

		switch command[0] {
		case "put":
			val_y := command[2]
			ind_y := hash(val_y, size)
			hash_table[index_x].put_x(key_x, ind_y, val_y)

		case "delete":
			val_y := command[2]
			ind_y := hash(val_y, size)
			hash_table[index_x].delete_y(key_x, ind_y, val_y)

		case "deleteall":
			hash_table[index_x].deleteall(key_x)

		case "get":
			f_out.WriteString(strings.Join(hash_table[index_x].get_ys(key_x), " "))
		}
	}
	f_out.Close()
}
