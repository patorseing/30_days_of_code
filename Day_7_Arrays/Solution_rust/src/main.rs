#![allow(non_snake_case)]
use std::io;

fn main() {
    let mut num = String::new();
    io::stdin().read_line(&mut num).expect("Failed to read line");
    // let n: i32 = num.replace("\n", "").parse().unwrap_or(0);

    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("Failed to read line");
    print!("{}", reverse(s.replace("\n", "")));
}

fn reverse(s: String) -> String {
    let my_str: &str = &s; //This is an &str type
    format!("{} ", my_str.chars().rev().collect::<String>())
}


#[cfg(test)] // Only compiles when running tests
mod tests {
    use super::reverse; // Import root greet function

    #[test]
    fn test_solve_caseI() {
        assert_eq!("2 3 4 1 ", reverse("1 4 3 2".to_owned()));
    }
}
