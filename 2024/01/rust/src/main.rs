use std::fs::read_to_string;
use std::iter::zip;

fn main() {
    let file = read_to_string("../../input").expect("Should have read file.");

    let lines = file.split("\n");
    let mut left: Vec<i32> = Vec::with_capacity(1000);
    let mut right: Vec<i32> = Vec::with_capacity(1000);

    for line in lines {
        if let Some((l, r)) = line.split_once("   ") {
            left.push(l.parse().expect("Correct parse."));
            right.push(r.parse().expect("Correct parse."));
        }
    }

    left.sort();
    right.sort();

    let part_1: i32 = zip(left, right).map(|(a, b)| (a - b).abs()).sum();
    println!("{part_1}");
}
