//
//  Solution_test.swift
//  Solution test
//
//  Created by Napatchol Thaipanich on 15/3/2564 BE.
//

@testable import Solution_swift
import XCTest

class Solution_test: XCTestCase {

    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    func testConcat() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        let solution = Solution()
        XCTAssertEqual("Hello, World. \nWelcome to 30 Days of Code!", solution.concat(str: "Welcome to 30 Days of Code!"))
    }

    func testPerformanceConcat() throws {
        // This is an example of a performance test case.
        let solution = Solution()
        measure {
            // Put the code you want to measure the time of here.
            let result = solution.concat(str: "Welcome to 30 Days of Code!")
            print(result)
        }
    }

}
