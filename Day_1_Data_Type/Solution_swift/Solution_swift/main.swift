//
//  main.swift
//  Solution_swift
//
//  Created by Napatchol Thaipanich on 30/3/2564 BE.
//

import Foundation

class Solution {
    func plusInt(inputI: Int) -> Int {
        let i = 4
        return inputI + i
    }
    
    func plusFloat(inputD: Double) -> Double {
        let d = 4.0
        return inputD + d
    }
    
    func concat(str: String) -> String {
        let s = "HackerRank "
        return s + str
    }
    
    func main() {
        // Declare second integer, double, and String variables.
        // Read and save an integer, double, and String to your variables.
        let inputI = Int(readLine()!)!
        let inputD = Double(readLine()!)!
        let inputS = readLine()!
        
        // Print the sum of both integer variables on a new line.
        print(plusInt(inputI: inputI))
        
        // Print the sum of the double variables on a new line.
        print(plusFloat(inputD:inputD))
        
        // Concatenate and print the String variables on a new line
        // The 's' variable above should be printed first.
        print(concat(str: inputS))
    }
}

let solution = Solution()
solution.main()
