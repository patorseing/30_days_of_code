//
//  main.swift
//  Solution_swift
//
//  Created by Napatchol Thaipanich on 8/4/2564 BE.
//

import Foundation

class Person {
    var age: Int = 0

    init(initialAge: Int) {
        // Add some more code to run some checks on initialAge
        if initialAge < 0 {
          print("Age is not valid, setting age to 0.")
        } else {
          age = initialAge
        }
    }
    
    func amIOldLigic() -> String {
        var str: String = ""
        if age < 0 {
            str = "Age is not valid, setting age to 0."
        } else if age < 13 {
            str = "You are young."
        } else if age >= 13 && age < 18 {
            str = "You are a teenager."
        } else {
            str = "You are old."
        }
        return str
    }

    func amIOld() {
        // Do some computations in here and print out the correct statement to the console
        print(amIOldLigic())
    }

    func yearPasses() {
        // Increment the age of the person in here
        age += 1
    }
}

let t = Int(readLine()!)!

for _ in 0..<t {
    let age = Int(readLine()!)!
    let p = Person(initialAge: age)

    p.amIOld()

    for _ in 1...3 {
        p.yearPasses()
    }

    p.amIOld()

    print("")
}

