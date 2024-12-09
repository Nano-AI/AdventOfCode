use std::fs;

fn calc_part_1(input: &Vec<u64>, index: i32, operator: char, val: u64) -> bool {
    if index as usize == input.len() {
        if val == *input.get(0).unwrap() {
            return true; 
        }
        return false;
    }
    let mut v: u64 = val;
    if operator == '*' {
        v *= input[index as usize]; 
    } else {
        v += input[index as usize];
    }
    return calc_part_1(input, index + 1, '*', v) || calc_part_1(input, index + 1, '+', v);
}

fn calc_size(num: u64) -> u32 {
    if num == 0 {
        return 1;
    }
    let mut size: u32 = 0;
    let mut test = num;
    while test > 0 {
        size += 1;
        test /= 10;
    }
    size
}

fn calc_part_2(input: &Vec<u64>, index: i32, operator: char, val: u64) -> bool {
    if index as usize == input.len() {
        return val == input[0];
    }
    let i = input[index as usize];
    if val > input[0] {
        return false;
    }
    let base: u64 = 10;
    let v: u64 = match operator {
        '*' => val * i,
        '+' => val + i,
        '|' => val * (base.pow(calc_size(i))) + i,
        _ => 0
    };
    return calc_part_2(input, index + 1, '*', v) || 
           calc_part_2(input, index + 1, '+', v) || 
           calc_part_2(input, index + 1, '|', v);
}

fn part_1(input: &Vec<Vec<u64>>) -> u64 {
    let mut total:  u64 = 0; 
    for line in input {
        let works = calc_part_1(line, 1, '+', 0) || calc_part_1(line, 1, '*', 0);
        if works {
            total += line.get(0).unwrap();
        }
    }
    return total;
}

fn part_2(input: &Vec<Vec<u64>>) -> u64 {
    let mut total: u64 = 0; 
    for line in input {
        let v1 = line[1];
        let works = calc_part_2(line, 2, '+', v1) || calc_part_2(line, 2, '*', v1) || calc_part_2(line, 2, '|', v1);
        if works {
            total += line[0];
        }
    }
    return total;
}

fn main() {
    // also possible to do a reversal technique by dividing to check divisibility (so you know it's multiplication)
    // check last digits for the | operator
    // and then use addition as a last resort

    let raw_input = fs::read_to_string("input.txt").unwrap();
    // who knows how rust works... i dont!
    let input: Vec<Vec<u64>> = raw_input.lines().map(|line| {
        let mut parts = line.split(':');
        let key = parts.next().unwrap_or("").trim()
            .parse::<u64>()
            .unwrap_or(0);
        let values = parts.next()
            .unwrap_or("")
            .split_whitespace()
            .filter_map(|num| num.parse::<u64>().ok())
            .collect::<Vec<u64>>();
        std::iter::once(key).chain(values.into_iter()).collect()
    }).collect();

    println!("Part 1: {}", part_1(&input));
    println!("Part 2: {}", part_2(&input));
}