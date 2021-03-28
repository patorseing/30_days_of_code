package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func plusInt(inInt uint64) uint64 {
	var i uint64 = 4
	return inInt + i
}

func plusFloat(inFloat float64) float64 {
	var i float64 = 4.0
	return inFloat + i
}

func concat(str string) string {
	return "HackerRank " + str
}

func main() {
	var _ = strconv.Itoa // Ignore this comment. You can still use the package "strconv".

	// var i uint64 = 4
	// var d float64 = 4.0
	// var s string = "HackerRank "

	scanner := bufio.NewScanner(os.Stdin)
	// Declare second integer, double, and String variables.
	var input_i uint64
	var input_d float64
	var input_s string

	// Read and save an integer, double, and String to your variables.
	fmt.Scanf("%d", &input_i)
	fmt.Scanf("%f", &input_d)
	scanner.Scan()
	input_s = scanner.Text()

	// Print the sum of both integer variables on a new line.
	// fmt.Println(i + input_i)
	fmt.Println(plusInt(input_i))
	// Print the sum of the double variables on a new line.
	// fmt.Printf("%.1f\n", d+input_d)
	fmt.Println(plusFloat(input_d))
	// Concatenate and print the String variables on a new line
	// The 's' variable above should be printed first.
	// fmt.Println(s + input_s)
	fmt.Println(concat(input_s))
}
