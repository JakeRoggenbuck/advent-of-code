use std::fs::read_to_string;

fn main() {
    let file = read_to_string("../../input").expect("read");

    let lines = file.split("\n");
    let mut left: Vec<&str> = Vec::with_capacity(1000);
    let mut right: Vec<&str> = Vec::with_capacity(1000);

    for line in lines {
        if let Some((l, r)) = line.split_once("   ") {
            left.push(l);
            right.push(r);
        }
    }

    println!("{:?} {:?}", left, right);
}
