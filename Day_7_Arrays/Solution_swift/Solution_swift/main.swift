//
//  main.swift
//  Solution_swift
//
//  Created by Napatchol Thaipanich on 4/10/2564 BE.
//

import Foundation

guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

guard let arrTemp = readLine() else { fatalError("Bad input") }

func reverse(arrTemp:String, n: Int) -> String {
    let arr: [Int] = arrTemp.split(separator: " ").map {
        if let arrItem = Int($0.trimmingCharacters(in: .whitespacesAndNewlines)) {
            return arrItem
        } else { fatalError("Bad input") }
    }

    guard arr.count == n else { fatalError("Bad input") }

    return Array(arr.reversed()).map { String($0) }.joined(separator: " ")
}

print(reverse(arrTemp: arrTemp, n: n))

