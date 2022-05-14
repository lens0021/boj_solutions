use std::io::{self, Read};

fn main() {
    let mut stdin = io::stdin();
    let mut buffer = String::new();

    // Read the size from stdin
    stdin.read_line(&mut buffer).expect("Failed");
    let size: usize = buffer.trim().parse::<usize>().unwrap();

    // Read the hay bales from stdin
    let mut heights = Vec::with_capacity(size);
    buffer.clear();
    stdin.read_to_string(&mut buffer).expect("Failed");
    heights.extend(buffer.split_whitespace().map(|x| x.parse::<u32>().unwrap()));

    let average = heights.iter().sum::<u32>() / heights.len() as u32;
    let net_diff = heights.iter().map(|h| h.saturating_sub(average)).sum::<u32>();
    println!("{}", net_diff);
}
