package main

import (
	"bytes"
	"fmt"
)

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	var count int
	fmt.Scan(&count)
	for i := 0; i < count; i++ {
		var str string
		fmt.Scan(&str)
		// var first string
		var first bytes.Buffer
		// var second string
		var second bytes.Buffer
		for j, ch := range str {
			if j%2 == 0 {
				first.WriteRune(ch)
			} else {
				second.WriteRune(ch)
			}
		}
		fmt.Println(first.String() + " " + second.String())
	}
}
