package main

import (
	"testing"
)

func TestConcat(t *testing.T) {
	t.Log(concat("Napatchol"))

	t.Run("pass", func(t *testing.T) {
		if concat("Napatchol") != "Hello, World.\nNapatchol" {
			t.Fatal("fail!")
		}
	})
	t.Run("fail", func(t *testing.T) {
		if concat("Napatchol") != "Hello, World.\nOx" {
			t.Errorf("expected %s but got %s", "Hello, World.\nOx", concat("Napatchol"))
			t.Fatal("fail!")
		}
	})
}
