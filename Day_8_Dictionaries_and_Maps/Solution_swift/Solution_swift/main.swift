//
//  main.swift
//  Solution_swift
//
//  Created by Napatchol Thaipanich on 29/10/2564 BE.
//

import Foundation

let phoneBook = PhoneBook.init(phone: [:])

var n = Int(readLine()!) // assume you enter your Name

for _ in 1 ... n! {
    let arg = readLine()!.split(separator: " ")
    phoneBook.add(key: String(arg[0]), val: String(arg[1]))
}

if let input = readLine() {
    var name = String(input)

    repeat {
        print(phoneBook.getByKey(key: name))

        if let input = readLine() {
            name = String(input)
        } else {
            name = ""
        }

    } while name.count > 0
}
