use std::fs;
use regex::Regex;

fn part_1(input : &str) -> i32 {
    let re = Regex::new(r"mul\((?<num1>\w+),(?<num2>\w+)\)").unwrap();
    let mut out = 0;
    for capture in re.captures_iter(input) {
        let num1 = &capture["num1"].parse::<i32>().unwrap();
        let num2 = &capture["num2"].parse::<i32>().unwrap();
        out += num1 * num2;
    }
    return out;
}

fn part_2(input: &str) -> i32 {
    let re = Regex::new(r"do\(\)|don't\(\)|mul\((?<num1>\w+),(?<num2>\w+)\)").unwrap();
    let mut out = 0;
    let mut enable = true;
    for capture in re.captures_iter(input) {
        match &capture[0] {
            "don't()" => {
                enable = false;
            }
            "do()" => {
                enable = true;
            }
            _ => {
                if enable {
                    let num1 = &capture["num1"].parse::<i32>().unwrap();
                    let num2 = &capture["num2"].parse::<i32>().unwrap();
                    out += num1 * num2;
                }
            }
        }
    }
    return out;
}

fn main() {
    let file_path = "test.txt";
    let input = fs::read_to_string(file_path).expect(format!("Can't read file {}", file_path).as_str());
    println!("Part 1: {}", part_1(input.as_str()));
    println!("Part 2: {}", part_2(input.as_str()));
}
