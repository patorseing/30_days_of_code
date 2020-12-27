import Foundation



guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

guard let arrTemp = readLine() else { fatalError("Bad input") }
let arr: [Int] = arrTemp.split(separator: " ").map {
    if let arrItem = Int($0.trimmingCharacters(in: .whitespacesAndNewlines)) {
        return arrItem
    } else { fatalError("Bad input") }
}

guard arr.count == n else { fatalError("Bad input") }

// for i in (0 ..< arr.count).reversed() {
//     print(arr[i]) // 4,3,2,1,0
// }

// for element in arr.reversed() {
//     print(element) // e,d,c,b,a
// }

// arr.reversed().forEach { print($0) } // e,d,c,b,a
// var stringReversedArray = Array(arr.map {
//   (number: Int) -> String in
//   return String(number)
// }.reversed()).joined(separator:" ")
// print(stringReversedArray) // e,d,c,b,a

print(Array(arr.reversed()).map { String($0) }.joined(separator: " "))
