use std::io;

fn main() {
    let mut n = String::new();
    io::stdin()
        .read_line(&mut n)
        .expect("Failed to read line");
        print!("{}",solve(n))
}

fn solve(n: String) -> String {
    let num : i32 = n.replace("\n", "").parse().unwrap_or(0);
    let result;
    if num % 2 == 1 {
        result = "Weird".to_owned();
    } else {
        if num > 1 && num < 6 {
            result = "Not Weird".to_owned();
        } else if num > 5 && num < 21 {
            result = "Weird".to_owned();
        } else {
            result = "Not Weird".to_owned();
        }
    }
    format!("{}", result)
}

#[cfg(test)] // Only compiles when running tests
mod tests {
    use super::solve; // Import root greet function

    #[test]
    fn test_solve_weird() {
        assert_eq!("Weird", solve("3".to_owned()));
    }

    #[test]
    fn test_solve_not_weird() {
        assert_eq!("Not Weird", solve("24".to_owned()));
    }
}
