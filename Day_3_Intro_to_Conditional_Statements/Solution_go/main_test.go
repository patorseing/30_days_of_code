package main

import (
	"testing"
)

func TestCalWeird(t *testing.T) {
	t.Run("Weird", func(t *testing.T) {
		if CalWeird(3) != "Weird" {
			t.Fatal("fail!", CalWeird(3))
		}
	})
}

func TestCalNotWeird(t *testing.T) {
	t.Run("Not Weird", func(t *testing.T) {
		if CalWeird(24) != "Not Weird" {
			t.Fatal("fail!", CalWeird(24))
		}
	})
}
