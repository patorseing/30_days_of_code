// package main

// import "fmt"

// func main() {
// 	//Enter your code here. Read input from STDIN. Print output to STDOUT
// 	var n int
// 	var name string
// 	var number string
// 	_, err := fmt.Scanf("%d", &n)

// 	if err != nil {
// 		return
// 	}

// 	phoneBook := make(map[string]string)

// 	for i := 0; i < n; i++ {
// 		_, err := fmt.Scanf("%s %s", &name, &number)

// 		if err != nil {
// 			return
// 		}

// 		phoneBook[name] = number
// 	}

// 	for true {
// 		var search string
// 		fmt.Scanf("%s", &search)
// 		if search == "" {
// 			break
// 		}

// 		if phoneBook[search] == "" {
// 			fmt.Println("Not found")
// 		} else {
// 			fmt.Printf("%s=%s\n", search, phoneBook[search])
// 		}
// 	}
// }

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Ref: https://github.com/sagarchoudhary96/30-Days-Of-Code/blob/master/Day8/Solution.go
func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Scan()
	n, _ := strconv.Atoi(in.Text())

	phoneBook := make(map[string]int)

	for i := 0; i < n; i++ {
		in.Scan()
		input := in.Text()
		values := strings.Split(input, " ")
		name := values[0]
		phone, _ := strconv.Atoi(values[1])

		phoneBook[name] = phone
	}

	for {
		in.Scan()
		key := in.Text()
		if key == "" {
			break
		}

		if value, ok := phoneBook[key]; ok {
			fmt.Printf("%s=%d\n", key, value)
		} else {
			fmt.Println("Not found")
		}
	}
}
