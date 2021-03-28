package main

import (
	"testing"
)

func TestPlusInt(t *testing.T) {
	t.Run("4", func(t *testing.T) {
		if plusInt(12) != 16 {
			t.Fatal("fail!")
		}
	})
}

func TestPlusFloat(t *testing.T) {
	t.Run("4.0", func(t *testing.T) {
		if plusFloat(4.0) != 8.0 {
			t.Fatal("fail!")
		}
	})
}

func TestConcat(t *testing.T) {
	t.Run("is the best place to learn and practice coding!", func(t *testing.T) {
		if concat("is the best place to learn and practice coding!") != "HackerRank is the best place to learn and practice coding!" {
			t.Fatal("fail!")
		}
	})
}
