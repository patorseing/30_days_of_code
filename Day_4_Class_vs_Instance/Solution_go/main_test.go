package main

import (
	"testing"
)

func TestPersonCaseI(t *testing.T) {
	age := -1
	p := person{age: age}
	p = p.NewPerson(age)
	t.Run("CheckAge", func(t *testing.T) {
		if CheckAge(age) != true {
			t.Fatal("fail!", CheckAge(-1))
		}
	})

	t.Run("amIOld", func(t *testing.T) {
		if p.amIOld() != "You are young." {
			t.Fatal("fail!", p.amIOld())
		}
	})

	t.Run("amIOldLast", func(t *testing.T) {
		for j := 0; j < 3; j++ {
			p = p.yearPasses()
		}
		if p.amIOld() != "You are young." {
			t.Fatal("fail!", p.amIOld())
		}
	})
}

func TestPersonCaseII(t *testing.T) {
	age := 10
	p := person{age: age}
	p = p.NewPerson(age)
	t.Run("CheckAge", func(t *testing.T) {
		if CheckAge(age) != false {
			t.Fatal("fail!", CheckAge(age))
		}
	})

	t.Run("amIOld", func(t *testing.T) {
		if p.amIOld() != "You are young." {
			t.Fatal("fail!", p.amIOld())
		}
	})

	t.Run("amIOldLast", func(t *testing.T) {
		for j := 0; j < 3; j++ {
			p = p.yearPasses()
		}
		if p.amIOld() != "You are a teenager." {
			t.Fatal("fail!", p.amIOld())
		}
	})
}

func TestPersonCaseIII(t *testing.T) {
	age := 16
	p := person{age: age}
	p = p.NewPerson(age)
	t.Run("CheckAge", func(t *testing.T) {
		if CheckAge(age) != false {
			t.Fatal("fail!", CheckAge(age))
		}
	})

	t.Run("amIOld", func(t *testing.T) {
		if p.amIOld() != "You are a teenager." {
			t.Fatal("fail!", p.amIOld())
		}
	})

	t.Run("amIOldLast", func(t *testing.T) {
		for j := 0; j < 3; j++ {
			p = p.yearPasses()
		}
		if p.amIOld() != "You are old." {
			t.Fatal("fail!", p.amIOld())
		}
	})
}

func TestPersonCaseIV(t *testing.T) {
	age := 18
	p := person{age: age}
	p = p.NewPerson(age)
	t.Run("CheckAge", func(t *testing.T) {
		if CheckAge(age) != false {
			t.Fatal("fail!", CheckAge(age))
		}
	})

	t.Run("amIOld", func(t *testing.T) {
		if p.amIOld() != "You are old." {
			t.Fatal("fail!", p.amIOld())
		}
	})

	t.Run("amIOldLast", func(t *testing.T) {
		for j := 0; j < 3; j++ {
			p = p.yearPasses()
		}
		if p.amIOld() != "You are old." {
			t.Fatal("fail!", p.amIOld())
		}
	})
}
