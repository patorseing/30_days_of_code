// Enter your code here
use std::io;

fn main() {
    let mut guess = String::new();
    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");
    println!("Hello, World.");
    print!("{}", guess);
}