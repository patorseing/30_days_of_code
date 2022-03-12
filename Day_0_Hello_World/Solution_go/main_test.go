package main

import (
	"fmt"
	"testing"
)

func TestConcat(t *testing.T) {
	t.Run("Welcome to 30 Days of Code!", func(t *testing.T) {
		fmt.Println(concat("Welcome to 30 Days of Code!"))
		if concat("Welcome to 30 Days of Code!") != "Hello, World.\nWelcome to 30 Days of Code!" {
			t.Fatal("fail!")
		}
	})
}
