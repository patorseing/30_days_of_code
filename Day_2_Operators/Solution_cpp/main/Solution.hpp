using namespace std;

int solve(double meal_cost, int tip_percent, int tax_percent) {
    double tip = meal_cost * ((double) tip_percent / 100);
    double tax = meal_cost * ((double) tax_percent / 100);
    int totalCost = meal_cost + tip + tax;

    // cout << totalCost << endl;
    return totalCost;
}
