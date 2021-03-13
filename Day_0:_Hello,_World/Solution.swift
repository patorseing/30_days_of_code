class Solution {
    func concat(str: String) -> String {
        return "Hello, World. \n" + str
    }

    func main() {
        let inputString = readLine()! // get a line of input from stdin and save it to our variable

        // Your first line of output goes here
        // print("Hello, World.")

        // // Write the second line of output
        // print(inputString)

        print(concat(str: inputString))
    }
}

let solution = Solution()
solution.main()
