use std::io;

fn main() {
  let mut line = String::new();
  io::stdin().read_line(&mut line).expect("err");

  let num:i32 = line.trim().parse::<i32>().unwrap();

  let mut factorial = 1;
  for i in 1..num+1 {
    factorial *= i;
  }
  print!("{}", factorial);
}
