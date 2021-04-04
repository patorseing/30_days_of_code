//
//  Solution_test.swift
//  Solution_test
//
//  Created by Napatchol Thaipanich on 4/4/2564 BE.
//

@testable import Solution_swift
import XCTest

class Solution_test: XCTestCase {

    let solution = Solution()
    
    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    func testWeird() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        XCTAssertEqual("Weird", solution.solve(N: 3))
    }
    
    func testNotWeird() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        XCTAssertEqual("Not Weird", solution.solve(N: 24))
    }

    func testPerformanceExample() throws {
        // This is an example of a performance test case.
        measure {
            // Put the code you want to measure the time of here.
            print(solution.solve(N: 3))
        }
    }

}
