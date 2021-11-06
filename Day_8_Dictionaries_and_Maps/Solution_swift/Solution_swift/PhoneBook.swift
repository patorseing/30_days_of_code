//
//  PhoneBook.swift
//  Solution_swift
//
//  Created by Napatchol Thaipanich on 29/10/2564 BE.
//

import Foundation

class PhoneBook {
    var phone: [String: String]
    
    init(phone: [String: String]) {
        self.phone = phone
    }
    
    func add (key: String, val: String) {
        self.phone[key] = val
    }
    
    func getAll () -> [String: String] {
        return self.phone
    }
    
    func getByKey (key: String) -> String {
        var res: String
        if let number = self.phone[key] {
            res = "\(key)=\(number)"
        } else {
            res = "Not found"
        }
        return res
    }
    
}
