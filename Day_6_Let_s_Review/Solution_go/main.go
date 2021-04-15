// https://github.com/xeoneux/30-Days-of-Code/blob/master/6%20-%20Let's%20Review/Solution.go
package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strings"
)

const (
	EVEN = iota
	ODD
)

func splitEvenNOdd(oddOrEven int, words string) string {
	var buffer = bytes.NewBufferString("")
	for i := oddOrEven; i < len(words); i += 2 {
		buffer.WriteByte(words[i])
	}
	return buffer.String() + " "
}

func print(oddOrEven int, words string) {
	fmt.Print(splitEvenNOdd(oddOrEven, words))
}

func main() {
	var T int

	fmt.Scan(&T)
	words := make([]string, T)
	reader := bufio.NewReader(os.Stdin)

	for i := 0; i < T; i++ {
		words[i], _ = reader.ReadString('\n')
		words[i] = strings.TrimSuffix(words[i], "\n")
	}

	for k := range words {
		print(EVEN, words[k])
		print(ODD, words[k])
		fmt.Printf("\n")
	}

}
