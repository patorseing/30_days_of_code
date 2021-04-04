//
//  main.swift
//  Solution_swift
//
//  Created by Napatchol Thaipanich on 4/4/2564 BE.
//

import Foundation

class Solution {
    
    func main() {
        let N = Int(readLine()!)! // get a line of input from stdin and save it to our variable
        
        // Your first line of output goes here
        // print("Hello, World.")
        
        // // Write the second line of output
        // print(inputString)
        
        print(solve(N: N))
    }
    
    func solve(N: Int) -> String {
        var result = ""
        if N % 2 == 1 {
            result = "Weird"
        } else {
            
            if N > 1 && N < 6 {
                result = "Not Weird"
            } else if N > 5 && N < 21 {
                result = "Weird"
            } else {
                result = "Not Weird"
            }
            
        }
        return result
    }
}

let solution = Solution()
solution.main()
