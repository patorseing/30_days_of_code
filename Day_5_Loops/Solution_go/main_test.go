package main

import (
	"testing"
)

func TestCase2(t *testing.T) {
	t.Run("2x1", func(t *testing.T) {
		if solve(2, 1) != "2 x 1 = 2" {
			t.Fatal("fail!", solve(2, 1))
		}
	})

	t.Run("2x2", func(t *testing.T) {
		if solve(2, 2) != "2 x 2 = 4" {
			t.Fatal("fail!", solve(2, 2))
		}
	})

	t.Run("2x3", func(t *testing.T) {
		if solve(2, 3) != "2 x 3 = 6" {
			t.Fatal("fail!", solve(2, 3))
		}
	})

	t.Run("2x4", func(t *testing.T) {
		if solve(2, 4) != "2 x 4 = 8" {
			t.Fatal("fail!", solve(2, 4))
		}
	})

	t.Run("2x5", func(t *testing.T) {
		if solve(2, 5) != "2 x 5 = 10" {
			t.Fatal("fail!", solve(2, 5))
		}
	})
}
