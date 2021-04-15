package main

import (
	"testing"
)

func TestCaseEven(t *testing.T) {
	t.Run("Hacker", func(t *testing.T) {
		if splitEvenNOdd(EVEN, "Hacker") != "Hce " {
			t.Fatal("fail!", splitEvenNOdd(EVEN, "Hacker"))
		}
	})

	t.Run("Rank", func(t *testing.T) {
		if splitEvenNOdd(EVEN, "Rank") != "Rn " {
			t.Fatal("fail!", splitEvenNOdd(EVEN, "Rank"))
		}
	})
}

func TestCaseOdd(t *testing.T) {
	t.Run("Hacker", func(t *testing.T) {
		if splitEvenNOdd(ODD, "Hacker") != "akr " {
			t.Fatal("fail!", splitEvenNOdd(EVEN, "Hacker"))
		}
	})

	t.Run("Rank", func(t *testing.T) {
		if splitEvenNOdd(ODD, "Rank") != "ak " {
			t.Fatal("fail!", splitEvenNOdd(EVEN, "Rank"))
		}
	})
}
