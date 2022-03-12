package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	in := bufio.NewReader(os.Stdin)

	inputString, _ := in.ReadString('\n')

	fmt.Print(concat(inputString))
}

func concat(inputString string) string {
	return "Hello, World." + "\n" + inputString
}
