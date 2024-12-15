use std::collections::HashMap;
use std::fs;

// calcualte num of digits through log & flooring
fn number_of_digits(n: u64) -> u32 {
    if n == 0 {
        1
    } else {
        (n as f64).log10().floor() as u32 + 1
    }
}

// udpate map
fn update_map(val: u64, increment: u64, map: &mut HashMap<u64, u64>) {
    *map.entry(val).or_insert(0) += increment;
}

// process the stones
fn process_stones(map: &HashMap<u64, u64>) -> HashMap<u64, u64> {
    // setup a hashmap
    let mut new_map = HashMap::new();
    // iterate through the hashmap
    for (&value, &count) in map.iter() {
        // check the # of digits
        let digits = number_of_digits(value);
        // store values of new map based on increment
        if value == 0 {
            update_map(1, count, &mut new_map);
        } else if digits % 2 == 0 {
            let increment = 10_u64.pow((digits / 2) as u32);
            let val1 = value / increment;
            let val2 = value % increment;
            update_map(val1, count, &mut new_map);
            update_map(val2, count, &mut new_map);
        } else {
            let new_value = value.checked_mul(2024).expect("Value overflowed");
            update_map(new_value, count, &mut new_map);
        }
    }
    // return map
    new_map
}

fn part_1(raw_values: Vec<u64>, iters: usize) -> usize {
    let mut map: HashMap<u64, u64> = HashMap::new();
    // set the base map
    for &val in raw_values.iter() {
        update_map(val, 1, &mut map);
    }
    // process every stone on the map
    for _ in 0..iters {
        map = process_stones(&map);
    }
    // sum the # of stones
    map.values().sum::<u64>() as usize
}

// this is me at 1:30 AM...
// exhausted but glad this works!
fn main() {
    let input: Vec<u64> = fs::read_to_string("input.txt")
        .expect("Can't read input file")
        .split_whitespace()
        .map(|v| v.parse::<u64>().expect("Failed to parse number"))
        .collect();

    println!("Part 1: {}", part_1(input.clone(), 25));
    println!("Part 2: {}", part_1(input.clone(), 75));
}
