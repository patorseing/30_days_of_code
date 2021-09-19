package main

import (
	"testing"
)

func TestCaseFound(t *testing.T) {
	phoneBook := map[string]int{"sam": 99912222, "tom": 11122222, "harry": 12299933}

	t.Run("sam", func(t *testing.T) {
		if findPhoneBook(phoneBook, "sam") != "sam=99912222" {
			t.Fatal("fail!", findPhoneBook(phoneBook, "sam"))
		}
	})
}

func TestCaseNotFound(t *testing.T) {
	phoneBook := map[string]int{"sam": 99912222, "tom": 11122222, "harry": 12299933}

	t.Run("edward", func(t *testing.T) {
		if findPhoneBook(phoneBook, "edward") != "Not found" {
			t.Fatal("fail!", findPhoneBook(phoneBook, "edward"))
		}
	})
}
