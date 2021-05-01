package main

import (
	"testing"
)

func TestCaseOdd(t *testing.T) {
	problem := []int32{1, 4, 3, 2}
	t.Run("1 4 3 2", func(t *testing.T) {
		if reverse(problem) != "2 3 4 1 " {
			t.Fatal("fail!", reverse(problem))
		}
	})
}
