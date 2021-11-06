//
//  Solution_test.swift
//  Solution_test
//
//  Created by Napatchol Thaipanich on 29/10/2564 BE.
//

import XCTest
@testable import Solution_swift

class Solution_test: XCTestCase {
    
    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }
    
    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }
    
    func testExist() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        let phoneBook = PhoneBook.init(phone: ["sam":"99912222", "tom":"11122222", "harry":"12299933"])
        XCTAssertEqual(phoneBook.getByKey(key: "sam"), "sam=99912222")
    }
    
    func testNotExist() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        let phoneBook = PhoneBook.init(phone: ["sam":"99912222", "tom":"11122222", "harry":"12299933"])
        XCTAssertEqual(phoneBook.getByKey(key: "edward"), "Not found")
    }
    
    func testBigTestcase() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        let phoneBook = PhoneBook.init(phone: [:])
        
        let testcaseFile =  Bundle.path(forResource: "testcase", ofType: "txt", inDirectory: ".")
        let testcase = try String(contentsOfFile: testcaseFile!, encoding: String.Encoding.utf8)
        let testcaseLines = testcase.components(separatedBy: .newlines)
        
        let resultFile =  Bundle.path(forResource: "result", ofType: "txt", inDirectory: ".")
        let result = try String(contentsOfFile: resultFile!, encoding: String.Encoding.utf8)
        let resultLines = result.components(separatedBy: .newlines)
        
        let totalInput = Int(testcaseLines[0]) ?? 0
        
        for index in 1...totalInput {
            let phone = testcaseLines[index].components(separatedBy: " ")
            phoneBook.add(key: phone[0], val: phone[1])
        }
        
        var resultIndex = 0
        
        for index in totalInput+1..<testcaseLines.count-1 {
            if resultLines[resultIndex] != phoneBook.getByKey(key: testcaseLines[index]) {
                XCTFail()
            }
            resultIndex = resultIndex + 1
        }
    }
    
    func testPerformanceExample() throws {
        // This is an example of a performance test case.
        measure {
            // Put the code you want to measure the time of here.
            do {
                let phoneBook = PhoneBook.init(phone: [:])
                
                let testcaseFile =  Bundle.path(forResource: "testcase", ofType: "txt", inDirectory: ".")
                let testcase = try String(contentsOfFile: testcaseFile!, encoding: String.Encoding.utf8)
                let testcaseLines = testcase.components(separatedBy: .newlines)
                
                let resultFile =  Bundle.path(forResource: "result", ofType: "txt", inDirectory: ".")
                let result = try String(contentsOfFile: resultFile!, encoding: String.Encoding.utf8)
                let resultLines = result.components(separatedBy: .newlines)
                
                let totalInput = Int(testcaseLines[0]) ?? 0
                
                for index in 1...totalInput {
                    let phone = testcaseLines[index].components(separatedBy: " ")
                    phoneBook.add(key: phone[0], val: phone[1])
                }
                
                var resultIndex = 0
                
                for index in totalInput+1..<testcaseLines.count-1 {
                    print(phoneBook.getByKey(key: testcaseLines[index]))
                    resultIndex = resultIndex + 1
                }
            } catch let error as NSError {
                print("Fail: \(error.localizedDescription)")
            } catch {
                print("Fail: \(error)")
            }
        }
    }
    
}
