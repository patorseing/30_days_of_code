import Foundation

// Complete the solve function below.
//func solve(meal_cost: Double, tip_percent: Int, tax_percent: Int) -> Void {
func solve(meal_cost: Double, tip_percent: Int, tax_percent: Int) -> Int {
    let tip = meal_cost * (Double(tip_percent) / 100)
    let tax = meal_cost * (Double(tax_percent) / 100)
    let totalCost = Int(meal_cost + tip + tax)
    print(totalCost)
    return totalCost
}

guard let meal_cost = Double((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

guard let tip_percent = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

guard let tax_percent = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

solve(meal_cost: meal_cost, tip_percent: tip_percent, tax_percent: tax_percent)
