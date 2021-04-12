//
//  main.swift
//  Solution_swift
//
//  Created by Napatchol Thaipanich on 13/4/2564 BE.
//

import Foundation

class Solution {
    
    func main() {
        let N = Int(readLine()!)! // get a line of input from stdin and save it to our variable
        
        // Your first line of output goes here
        // print("Hello, World.")
        
        // // Write the second line of output
        // print(inputString)
        for i in 1...10 {
            print(solve(N: N, i: i))
        }
    }
    
    func solve(N: Int, i: Int) -> String {
        return "\(N) x \(i) = \(N*i)"
    }
}

let solution = Solution()
solution.main()
