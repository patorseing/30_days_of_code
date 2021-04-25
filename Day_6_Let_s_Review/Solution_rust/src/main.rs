#![allow(non_snake_case)]
use std::io;

fn main() {
    let mut num = String::new();
    io::stdin().read_line(&mut num).expect("Failed to read line");
    let t: i32 = num.replace("\n", "").parse().unwrap_or(0);

    let mut words = Vec::new();
    for _elem in 0..t {
        let mut word = String::new();
        io::stdin().read_line(&mut word).expect("Failed to read line");
        words.push(word.replace("\n", ""));
    }

    for word in words {
        println!("{}", solve(word));
    }
}

fn solve(word: String) -> String {
    let mut first = String::new();
    let mut second = String::new();
    for (i, c) in word.chars().enumerate() {
        if i % 2 == 0 {
            first.push(c);
          } else {
            second.push(c);
          }
    }
    format!("{}", format!("{} {}", first, second))
}

#[cfg(test)] // Only compiles when running tests
mod tests {
    use super::solve; // Import root greet function

    #[test]
    fn test_solve_caseI() {
        assert_eq!("Hce akr", solve("Hacker".to_owned()));
    }

    #[test]
    fn test_solve_caseII() {
        assert_eq!("Rn ak", solve("Rank".to_owned()));
    }
}
