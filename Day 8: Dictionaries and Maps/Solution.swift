// Enter your code here. Read input from STDIN. Print output to STDOUT
var phoneBook = [String: String]()
var n = Int(readLine()!) // assume you enter your Name

for _ in 1 ... n! {
    let arg = readLine()!.split(separator: " ")
    phoneBook[String(arg[0])] = String(arg[1])
}

// var search = String(readLine()!)
// while search != "" {
//     // for _ in 1 ... n! {
//     if let _ = myMap[search] {
//         // now val is not nil and the Optional has been unwrapped, so use it
//         print(search + "=" + myMap[search]!)
//     } else {
//         print("Not found")
//     }
//     search = String(readLine()!)
// }

if let input = readLine() {
        var name = String(input)

        repeat {
            if let phoneNumber = phoneBook[name] {
                print("\(name)=\(phoneNumber)")
            } else {
                print("Not found")
            }

            if let input = readLine() {
                name = String(input)
            } else {
                name = ""
            }

        } while name.count > 0
    }
