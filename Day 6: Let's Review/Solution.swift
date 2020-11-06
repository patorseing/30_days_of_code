import Darwin
import Foundation

let numStrings = Int(readLine()!)!

func printEvenAndOdd(string: String) {
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

    print(first + " " + second)
}

for _ in 1 ... numStrings {
    let inputString = readLine()!
    printEvenAndOdd(string: inputString)
}
