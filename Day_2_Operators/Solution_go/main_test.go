package main

import (
	"testing"
)

func TestCalCost1(t *testing.T) {
	t.Run("calCost 12.00, 20", func(t *testing.T) {
		if calCost(12.00, 20) != 2.40 {
			t.Fatal("fail!", calCost(12.00, 20))
		}
	})
}

func TestCalCost2(t *testing.T) {
	t.Run("calCost 12.00, 8", func(t *testing.T) {
		if calCost(12.00, 8) != 0.96 {
			t.Fatal("fail!", calCost(12.00, 8))
		}
	})
}

func TestCalTotalCost(t *testing.T) {
	t.Run("calTotalCost", func(t *testing.T) {
		if calTotalCost(12.00, calCost(12.00, 20), calCost(12.00, 8)) != 15 {
			t.Fatal("fail!", calTotalCost(12.00, calCost(12.00, 20), calCost(12.00, 8)))
		}
	})
}

func TestSolve(t *testing.T) {
	t.Run("solve", func(t *testing.T) {
		if solve(12.00, 20, 8) != 15 {
			t.Fatal("fail!")
		}
	})
}
