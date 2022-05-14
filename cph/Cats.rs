fn main() {
  let cat = r#"
\    /\
 )  ( ')
(  /  )
 \(__)|
"#;
  // Trims the whitespace from the beginning and end of the string
  println!("{}", cat.trim());
}
