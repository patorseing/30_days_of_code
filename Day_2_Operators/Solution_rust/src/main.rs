use std::io;

fn main() {
    let mut meal_cost = String::new();
    let mut tip_percent = String::new();
    let mut tax_percent = String::new();

    io::stdin()
        .read_line(&mut meal_cost)
        .expect("Failed to read line");
    io::stdin()
        .read_line(&mut tip_percent)
        .expect("Failed to read line");

    io::stdin()
        .read_line(&mut tax_percent)
        .expect("Failed to read line");

    print!("{}",solve(meal_cost, tip_percent, tax_percent))
}


fn solve(meal_cost: String, tip_percent: String, tax_percent: String) -> String {
    // print!("debug int {}", a);
    let cost : f32 = meal_cost.replace("\n", "").parse().unwrap_or(0.0);
    let tip : f32 = cost * (tip_percent.replace("\n", "").parse().unwrap_or(0) as f32 / 100 as f32);
    let tax : f32 = cost * (tax_percent.replace("\n", "").parse().unwrap_or(0) as f32 / 100 as f32);
    let total :f32 = (cost + tip +tax).round();
    // print!("after int {}\n", my_int);
    format!("{}", total)
}


#[cfg(test)] // Only compiles when running tests
mod tests {
    use super::solve; // Import root greet function

    #[test]
    fn test_solve_case_i() {
        assert_eq!("15", solve("12.00".to_owned(), "20".to_owned(), "8".to_owned()));
    }

    #[test]
    fn test_solve_case_iii() {
        assert_eq!("13", solve("10.25".to_owned(), "17".to_owned(), "5".to_owned()));
    }
}
