//
//  Solution_test.swift
//  Solution_test
//
//  Created by Napatchol Thaipanich on 13/4/2564 BE.
//

import XCTest
@testable import Solution_swift

class Solution_test: XCTestCase {

    let solution = Solution()
    
    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    func testSolveI() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        XCTAssertEqual("2 x 1 = 2", solution.solve(N: 2, i:1))
    }
    
    func testSolveII() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        XCTAssertEqual("2 x 2 = 4", solution.solve(N: 2, i:2))
    }

    func testPerformanceExample() throws {
        // This is an example of a performance test case.
        measure {
            // Put the code you want to measure the time of here.
            for i in 1...10 {
                print(solution.solve(N: 2, i: i))
            }
        }
    }

}
