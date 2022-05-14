use std::io;

fn read_line_and_parse_to_int() -> i32 {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    return input.trim().parse::<i32>().expect("Failed to parse input");
}

fn main() {
    // Reads the numbers from the standard input.
    let a = read_line_and_parse_to_int();
    let b = read_line_and_parse_to_int();
    // Prints input
    println!("{}", a * (b % 10));
    println!("{}", a * ((b /10) % 10));
    println!("{}", a * ((b /100) % 10));
    println!("{}", a * b);
}
