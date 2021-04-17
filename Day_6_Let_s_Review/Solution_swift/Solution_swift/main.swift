//
//  main.swift
//  Solution_swift
//
//  Created by Napatchol Thaipanich on 17/4/2564 BE.
//

import Darwin
import Foundation

let numStrings = Int(readLine()!)!

func EvenAndOdd(string: String) -> String {
    // This prints inputString to stderr for debugging:
    // Print the even-indexed characters
    // Write your code here

    var first = ""
    var second = ""
    for (index, char) in string.enumerated() {
        if index % 2 == 0 {
            first += String(char)
        } else {
            second += String(char)
        }
    }

    return first + " " + second
}

func printEvenAndOdd(string: String) {
    // This prints inputString to stderr for debugging:
    // Print the even-indexed characters
    // Write your code here

    print(EvenAndOdd(string: string))
}

for _ in 1 ... numStrings {
    let inputString = readLine()!
    printEvenAndOdd(string: inputString)
}
