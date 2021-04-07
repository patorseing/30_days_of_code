//
//  Solution_test.swift
//  Solution_test
//
//  Created by Napatchol Thaipanich on 8/4/2564 BE.
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

    func testCaseI() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        let age = -1
        let p = Person(initialAge: age)
        var actual = p.amIOldLigic()
        var expected = "You are young."
        XCTAssertEqual(actual, expected)
        for _ in 1...3 {
                p.yearPasses()
            }

        actual = p.amIOldLigic()
        expected = "You are young."
        XCTAssertEqual(actual, expected)
    }
    
    func testCaseII() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        let age = 10
        let p = Person(initialAge: age)
        var actual = p.amIOldLigic()
        var expected = "You are young."
        XCTAssertEqual(actual, expected)
        for _ in 1...3 {
                p.yearPasses()
            }

        actual = p.amIOldLigic()
        expected = "You are a teenager."
        XCTAssertEqual(actual, expected)
    }
    
    func testCaseIII() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        let age = 16
        let p = Person(initialAge: age)
        var actual = p.amIOldLigic()
        var expected = "You are a teenager."
        XCTAssertEqual(actual, expected)
        for _ in 1...3 {
                p.yearPasses()
            }

        actual = p.amIOldLigic()
        expected = "You are old."
        XCTAssertEqual(actual, expected)
    }
    
    func testCaseIV() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
        let age = 18
        let p = Person(initialAge: age)
        var actual = p.amIOldLigic()
        var expected = "You are old."
        XCTAssertEqual(actual, expected)
        for _ in 1...3 {
                p.yearPasses()
            }

        actual = p.amIOldLigic()
        expected = "You are old."
        XCTAssertEqual(actual, expected)
    }

    func testPerformanceExample() throws {
        // This is an example of a performance test case.
        measure {
            // Put the code you want to measure the time of here.
            let age = -1
            let p = Person(initialAge: age)

            p.amIOld()

            for _ in 1...3 {
                p.yearPasses()
            }

            p.amIOld()

            print("")
        }
    }

}
