use std::io;

fn main() {
    let mut input_int = String::new();
    let mut input_float = String::new();
    let mut input_str = String::new();

    io::stdin()
        .read_line(&mut input_int)
        .expect("Failed to read line");
    io::stdin()
        .read_line(&mut input_float)
        .expect("Failed to read line");

    io::stdin()
        .read_line(&mut input_str)
        .expect("Failed to read line");

    print!("{}\n", plus_int(input_int));
    print!("{}\n", plus_float(input_float));
    print!("{}", concat(input_str));
}


fn plus_int(a: String) -> String {
    // print!("debug int {}", a);
    let i = 4;
    let my_int : i32 = a.replace("\n", "").parse().unwrap_or(0);
    // print!("after int {}\n", my_int);
    format!("{}", my_int+i)
}

fn plus_float(a: String) -> String {
    // print!("debug float {}", a);
    let d = 4.0;
    let my_float : f32 = a.replace("\n", "").parse().unwrap_or(0.0);
    // print!("after float {}\n", my_float);
    format!("{:.1}", my_float + d)
}

fn concat(a: String) -> String {
    let result: String = "HackerRank ".to_owned();
    format!("{}{}", result, a)
}

#[cfg(test)] // Only compiles when running tests
mod tests {
    use super::plus_int; // Import root greet function
    use super::plus_float; // Import root greet function
    use super::concat; // Import root greet function

    #[test]
    fn test_plus_int() {
        assert_eq!("16", plus_int("12".to_owned()));
    }

    #[test]
    fn test_plus_float() {
        assert_eq!("8.0", plus_float("4.0".to_owned()));
    }

    #[test]
    fn test_concat() {
        assert_eq!("HackerRank is the best place to learn and practice coding!", concat("is the best place to learn and practice coding!".to_owned()));
    }
}
