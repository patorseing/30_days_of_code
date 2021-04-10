#![allow(non_snake_case)]

struct Person {
    age: i32,
}

impl Person {
    fn new(mut initialAge: i32) -> Person {
        // Add some more code to run some checks on initialAge
        if initialAge < 0 {
            println!("Age is not valid, setting age to 0.");
            initialAge = 0;
        }
        return Person { age: initialAge };
    }
    fn amIOldLogic(&self) -> String {
        // Do some computations in here and print out the correct statement to the console
        let str;
        if self.age < 0 {
            str = "Age is not valid, setting age to 0.".to_owned();
        } else if self.age < 13 {
            str = "You are young.".to_owned();
        } else if self.age >= 13 && self.age < 18 {
            str = "You are a teenager.".to_owned();
        } else {
            str = "You are old.".to_owned();
        }
        format!("{}", str)
    }
    fn amIOld(&self) {
        // Do some computations in here and print out the correct statement to the console
        println!("{}", self.amIOldLogic())
    }
    fn yearPasses(&mut self) {
        // Increment the age of the person in here
        self.age += 1;
    }
}

fn main() {
    let T: i32 = read_line().trim().parse().unwrap();
    for _ in 0..T {
        let age = read_line().trim().parse().unwrap();
        let mut p = Person::new(age);
        p.amIOld();
        for _ in 0..3 {
            p.yearPasses();
        }
        p.amIOld();
        println!("");
    }
}

fn read_line() -> String {
    let mut input = String::new();
    std::io::stdin()
        .read_line(&mut input)
        .expect("Could not read stdin!");
    return input;
}

#[cfg(test)] // Only compiles when running tests
mod tests {
    use super::Person;

    #[test]
    fn test_caseI() {
        let age = -1;
        let mut p = Person::new(age);
        assert_eq!("You are young.", p.amIOldLogic());
        for _ in 0..3 {
            p.yearPasses();
        }
        p.amIOld();
        assert_eq!("You are young.", p.amIOldLogic());
    }

    #[test]
    fn test_caseII() {
        let age = 10;
        let mut p = Person::new(age);
        assert_eq!("You are young.", p.amIOldLogic());
        for _ in 0..3 {
            p.yearPasses();
        }
        p.amIOld();
        assert_eq!("You are a teenager.", p.amIOldLogic());
    }

    #[test]
    fn test_caseIII() {
        let age = 16;
        let mut p = Person::new(age);
        assert_eq!("You are a teenager.", p.amIOldLogic());
        for _ in 0..3 {
            p.yearPasses();
        }
        p.amIOld();
        assert_eq!("You are old.", p.amIOldLogic());
    }

    #[test]
    fn test_caseIV() {
        let age = 18;
        let mut p = Person::new(age);
        assert_eq!("You are old.", p.amIOldLogic());
        for _ in 0..3 {
            p.yearPasses();
        }
        p.amIOld();
        assert_eq!("You are old.", p.amIOldLogic());
    }
}
