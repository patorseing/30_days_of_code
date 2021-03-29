//
//  Solution_test.swift
//  Solution test
//
//  Created by Napatchol Thaipanich on 30/3/2564 BE.
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
    
    func testPlusInt() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        let solution = Solution()
        XCTAssertEqual(16, solution.plusInt(inputI: 12))
    }
    
    func testPlusFloat() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        let solution = Solution()
        XCTAssertEqual(8.0, solution.plusFloat(inputD: 4.0))
    }

    func testConcat() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        let solution = Solution()
        XCTAssertEqual("HackerRank is the best place to learn and practice coding!", solution.concat(str: "is the best place to learn and practice coding!"))
    }

    func testPerformanceConcat() throws {
        // This is an example of a performance test case.
        let solution = Solution()
        measure {
            // Put the code you want to measure the time of here.
            print(solution.plusInt(inputI: 12))
            print(solution.plusFloat(inputD: 4.0))
            print(solution.concat(str: "is the best place to learn and practice coding!"))
        }
    }

}
