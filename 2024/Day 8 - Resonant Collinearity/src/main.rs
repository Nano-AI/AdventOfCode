use std::fs;
use std::collections::HashMap;

#[derive(Debug)]
struct vec2 {
    x: i32,
    y: i32
}

impl vec2 {
    fn equals(self: &vec2, v: &vec2) -> bool {
        self.x == v.x && self.y == v.y
    }

    fn minus(self: &vec2, v: &vec2) -> vec2 {
        vec2{x: self.x - v.x, y: self.y - v.y}
    }

    fn plus(self: &vec2, v: &vec2) -> vec2 {
        vec2{x: self.x + v.x, y: self.y + v.y}
    }

    fn copy(self: &vec2) -> vec2 {
        vec2{x: self.x, y: self.y}
    }
}

fn in_bounds(val: i32, min: i32, max: i32) -> bool {
    return val >= min && val < max;
}

fn part_1(mut input: Vec<Vec<char>>, iterative: bool) -> i32 {
    let mut pos: HashMap<char, Vec<vec2>> = HashMap::new();
    let height = input.len();
    let width = input[0].len();
    let mut count = 0;

    for j in 0..height {
        let line = &input[j];
        for i in 0..width {
            let c = line[i];
            if c == '.' {
                continue
            }
            if pos.contains_key(&c) {
                pos.get_mut(&c).unwrap().push(vec2{x: i as i32, y: j as i32});
            } else {
                pos.insert(c, vec![vec2{x: i as i32, y: j as i32}]);
            }
        }
    }

    for key in pos.keys() {
        let ps = &pos[key];
        for a1 in ps {
            for a2 in ps {
                if a1.equals(a2) {
                    continue;
                }

                if !iterative {
                    // from a2 to a1
                    let dp = a1.minus(a2);
                    // pos final
                    let pf = a2.minus(&dp);
                    if in_bounds(pf.x, 0, width as i32) && in_bounds(pf.y, 0, height as i32) {
                        let v = &input[pf.y as usize][pf.x as usize];
                        if *v != '#' {
                            count += 1;
                            input[pf.y as usize][pf.x as usize] = '#';
                        }
                    }
                } else {
                    // from a2 to a1
                    let dp = a1.minus(a2);
                    // pos final
                    let mut pf = a2.copy();
                    while in_bounds(pf.x, 0, width as i32) && in_bounds(pf.y, 0, height as i32) {
                        let v = &input[pf.y as usize][pf.x as usize];
                        if *v != '#' {
                            count += 1;
                            input[pf.y as usize][pf.x as usize] = '#';
                        }
                        pf.x -= dp.x;
                        pf.y -= dp.y;
                    }
                }
            }
        }
    }
    count
}

fn main() {
    let raw_input = fs::read_to_string("input.txt").unwrap();
    let input: Vec<Vec<char>> = raw_input.lines()
        .map(|line| {
            line.chars().collect()
        }).collect();
    println!("Part 1: {}", part_1(input.to_owned(), false));
    println!("Part 2: {}", part_1(input.to_owned(), true));
}
