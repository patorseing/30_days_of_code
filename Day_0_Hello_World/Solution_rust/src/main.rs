use std::io;

fn main() {
    let mut guess = String::new();
    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");
    // println!("Hello, World.");
    // print!("{}", guess);
    print!("{}", concat(guess));
}

fn concat (a: String) -> String {
    let result: String = "Hello, World.\n".to_owned();
    format!("{}{}", result, a)
}

#[cfg(test)] // Only compiles when running tests
mod tests {
    use super::concat; // Import root greet function

    #[test]
    fn test_greet() {
        assert_eq!("Hello, World.\nWelcome to 30 Days of Code!", concat("Welcome to 30 Days of Code!".to_owned()));
    }
}
