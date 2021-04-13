use std::io;

fn main() {
    let mut n = String::new();

    io::stdin().read_line(&mut n).expect("Failed to read line");
    let num: i32 = n.replace("\n", "").parse().unwrap_or(0);
    for elem in 1..11 {
        println!("{}", solve(num, elem));
    }
}

fn solve(n: i32, i: i32) -> String {
    format!("{}", format!("{} x {} = {}", n, i, n * i))
}

#[cfg(test)] // Only compiles when running tests
mod tests {
    use super::solve; // Import root greet function

    #[test]
    fn test_solve_weird() {
        assert_eq!("2 x 1 = 2", solve(2,1));
    }
}
