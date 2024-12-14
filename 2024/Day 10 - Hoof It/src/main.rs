use std::collections::{HashMap, HashSet};
use std::env;
use std::fs;

struct Map {
    grid: Vec<i32>,
    width: i32,
    height: i32,
}

impl Map {
    fn get(&self, x: i32, y: i32) -> i32 {
        if self.in_bound(x, y) {
            self.grid[(y * self.width + x) as usize]
        } else {
            panic!("Attempting to access out-of-bounds grid position ({}, {})", x, y);
        }
    }

    fn in_bound(&self, x: i32, y: i32) -> bool {
        x >= 0 && x < self.width && y >= 0 && y < self.height
    }
    
    fn new(input: String) -> Map {
        let mut grid = Vec::new();
        let mut width = 0;
        let mut height = 0;

        for line in input.lines() {
            width = line.len() as i32;
            height += 1;
            grid.extend(line.chars().map(|ch| ch.to_digit(10).unwrap() as i32));
        }

        Map {
            grid, 
            width, 
            height,
        }
    }
}

/// Returns the set of all reachable 9-height cells from the given starting cell (x, y).
fn reachable_nines(map: &Map, x: i32, y: i32, memo: &mut HashMap<(i32, i32), HashSet<(i32, i32)>>) -> HashSet<(i32, i32)> {
    // Check if we've already computed this
    if let Some(cached) = memo.get(&(x, y)) {
        return cached.clone();
    }

    let current_height = map.get(x, y);
    // Base case: if current cell is 9, the set is just this cell
    if current_height == 9 {
        let mut s = HashSet::new();
        s.insert((x, y));
        memo.insert((x, y), s.clone());
        return s;
    }

    // If height is less than 9, try to move to height + 1
    let directions = [(1, 0), (-1, 0), (0, -1), (0, 1)];
    let mut result_set = HashSet::new();

    for &(dx, dy) in &directions {
        let nx = x + dx;
        let ny = y + dy;
        if map.in_bound(nx, ny) && map.get(nx, ny) == current_height + 1 {
            let sub_result = reachable_nines(map, nx, ny, memo);
            // Union the sets
            for cell in sub_result {
                result_set.insert(cell);
            }
        }
    }

    // Store in memo before returning
    memo.insert((x, y), result_set.clone());
    result_set
}

fn count_paths(x: i32, y: i32, map: &Map, memo: &mut HashMap<(i32, i32), i32>) -> i32 {
    // Check if result is already computed
    if let Some(&cached) = memo.get(&(x, y)) {
        return cached;
    }

    let current_height = map.get(x, y);
    // Base case: if the current cell is height 9, only one valid path (end here)
    if current_height == 9 {
        memo.insert((x, y), 1);
        return 1;
    }

    let directions = [(1, 0), (-1, 0), (0, -1), (0, 1)];
    let mut total_paths = 0;

    for &(dx, dy) in &directions {
        let nx = x + dx;
        let ny = y + dy;
        if map.in_bound(nx, ny) && map.get(nx, ny) == current_height + 1 {
            total_paths += count_paths(nx, ny, map, memo);
        }
    }

    // Memoize and return the result
    memo.insert((x, y), total_paths);
    total_paths
}

fn main() {
    let input = fs::read_to_string("./input.txt").expect("Can't read input file");
    let map = Map::new(input);
    let mut total_rating = 0;
    let mut memo1 = HashMap::new();
    let mut memo2 = HashMap::new();
    let mut score = 0;

    for j in 0..map.height {
        for i in 0..map.width {
            if map.get(i, j) == 0 {
                let nine_cells = reachable_nines(&map, i, j, &mut memo1);
                score += nine_cells.len() as i32; 
                total_rating += count_paths(i, j, &map, &mut memo2);
            }
        }
    }

    println!("Part 1: {}", score);
    println!("Part 2: {}", total_rating);
}