use std::fs;

fn main() {
    let contents = fs::read_to_string("../../input").expect("File broke");

    let chars: Vec<char> = contents.chars().collect();
    let mut nums: Vec<i32> = Vec::new();

    let mut index: usize = 0;
    let mut current_num = String::new();
    let mut current: char;

    let mut last: i32;
    let mut num_increases: i32 = 0;

    while index < contents.len() {
        current = chars[index];
        if current == '\n' {
            nums.push(current_num.parse::<i32>().unwrap());
            current_num = String::new();
        } else {
            current_num.push(current);
        }
        index += 1;
    }
    
    last = nums[0];
    for x in nums {
        if x > last {
            num_increases += 1;
        }
        last = x;
    }
    println!("{}", num_increases);
}
