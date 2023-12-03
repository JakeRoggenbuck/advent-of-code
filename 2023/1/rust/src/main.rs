use regex::Regex;
use std::fs;
use std::path::Path;

fn check_path() -> Result<String, ()> {
    let paths = ["../input", "../../input"];

    for path in paths {
        if Path::new(path).exists() {
            return Ok(path.to_string());
        }
    }

    Err(())
}

fn two() {}

fn one() {
    let num = Regex::new(r"\d").unwrap();
    let path = check_path().unwrap();
    let content: String = fs::read_to_string(path).expect("Could not read input");

    let mut total = 0;

    for line in content.lines() {
        let matches: Vec<_> = num.find_iter(line).map(|m| m.as_str()).collect();
        let first = matches[0];
        let last = matches[matches.len() - 1];
        let sum = format!("{}{}", first, last);
        let sum_int = sum.parse::<i32>().unwrap();
        total += sum_int;
    }

    println!("{}", total);
}

fn main() {
    one();
    two();
}
