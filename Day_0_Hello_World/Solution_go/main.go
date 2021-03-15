package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func concat(str string) string {
	return "Hello, World.\n" + str
}

func main() {

	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	text = strings.Replace(text, "\n", "", -1)

	// fmt.Println("Hello, World.")
	// fmt.Println(text)
	fmt.Println(concat(text))
}
