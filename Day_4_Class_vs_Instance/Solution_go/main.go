package main

import "fmt"

type person struct {
	age int
}

func CheckAge(initialAge int) bool {
	if initialAge < 0 {
		return true
	}
	return false
}

func (p person) NewPerson(initialAge int) person {
	//Add some more code to run some checks on initialAge
	if CheckAge(initialAge) {
		fmt.Println("Age is not valid, setting age to 0.")
		p.age = 0
	} else {
		p.age = initialAge
	}
	return p
}

func (p person) amIOld() string {
	//Do some computation in here and print out the correct statement to the console
	str := ""
	if p.age < 0 {
		str = "Age is not valid, setting age to 0."
	} else if p.age < 13 {
		str = "You are young."
	} else if p.age >= 13 && p.age < 18 {
		str = "You are a teenager."
	} else {
		str = "You are old."
	}
	return str
}

func (p person) yearPasses() person {
	//Increment the age of the person in here
	p.age++
	return p
}

func main() {
	var T, age int

	fmt.Scan(&T)

	for i := 0; i < T; i++ {
		fmt.Scan(&age)
		p := person{age: age}
		p = p.NewPerson(age)
		fmt.Println(p.amIOld())
		for j := 0; j < 3; j++ {
			p = p.yearPasses()
		}
		fmt.Println(p.amIOld())
		fmt.Println()
	}
}
