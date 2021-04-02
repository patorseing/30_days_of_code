package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"strconv"
	"strings"
)

// Complete the solve function below.
func solve(meal_cost float64, tip_percent int32, tax_percent int32) float64 {
	var tip = calCost(meal_cost, tip_percent)
	var tax = calCost(meal_cost, tax_percent)
	var totalCost = calTotalCost(meal_cost, tip, tax)
	fmt.Println(math.Round(totalCost))
	return totalCost
}

func calCost(meal_cost float64, percent int32) float64 {
	return math.Round(meal_cost*(float64(percent)/100)*100) / 100
}

func calTotalCost(meal_cost float64, tip float64, tax float64) float64 {
	return math.Round(meal_cost + tip + tax)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	meal_cost, err := strconv.ParseFloat(readLine(reader), 64)
	checkError(err)

	tip_percentTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	tip_percent := int32(tip_percentTemp)

	tax_percentTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	tax_percent := int32(tax_percentTemp)

	solve(meal_cost, tip_percent, tax_percent)
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
