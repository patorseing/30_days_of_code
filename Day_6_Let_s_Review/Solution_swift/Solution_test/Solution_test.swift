//
//  Solution_test.swift
//  Solution_test
//
//  Created by Napatchol Thaipanich on 17/4/2564 BE.
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

    func testICase() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        XCTAssertEqual("Hce akr", EvenAndOdd(string:"Hacker"))
    }
    func testIICase() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        XCTAssertEqual("Rn ak", EvenAndOdd(string:"Rank"))
    }

    func testPerformanceExample() throws {
        // This is an example of a performance test case.
        measure {
            // Put the code you want to measure the time of here.
            print(EvenAndOdd(string:"Hacker"))
        }
    }

}
