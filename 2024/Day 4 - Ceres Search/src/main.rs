use std::fs;

fn search(grid: &Vec<Vec<char>>, x: i32, y: i32, x_dir: i32, y_dir: i32, index: i32, backwards: bool, width: i32, height: i32) -> bool {
    // recurisivley check to see if it makes a pattern in the given direction
    let m = if backwards {
        vec!['S', 'A', 'M', 'X']
    } else {
        vec!['X', 'M', 'A', 'S']
    };
    

    if index > 3 {
        return false;
    }

    if x < 0 || x >= width {
        return false;
    }
    if y < 0 || y >= height {
        return false;
    }

    if grid[x as usize][y as usize] == m[index as usize] {
        if index == 3 {
            return true
        }
        return search(grid, x + x_dir, y + y_dir, x_dir, y_dir, index + 1, backwards, width, height);
    }

    return false
}

fn part_1(input: &str) -> i32 {
    let grid: Vec<Vec<char>> = input.lines().map(|row: &str| row.chars().collect()).collect();
    let mut count = 0;
    let mut x: i32 = 0;
    let mut y: i32 = 0;

    let width: i32 = grid[0].len().try_into().unwrap();
    let height: i32 = grid.len().try_into().unwrap();

    while x <= width && y < height {
        if x == width {
            x -= width;
            y += 1;
        }

        if y >= height {
            break;
        }

        let c = grid[x as usize][y as usize];


        if c != 'X' && c != 'S' {
            x += 1;
            continue;
        }

        let backwards = c == 'S';

        // check for a pattern in all directions
        for x_dir in -1..=1 {
            for y_dir in -1..=1 {
                count += search(&grid, x, y, x_dir, y_dir, 0, backwards, width, height) as i32;
            }
        }
        x += 1;
    }
    return count;
}

fn part_2(input: &str) -> i32 {
    let grid: Vec<Vec<char>> = input.lines().map(|row: &str| row.chars().collect()).collect();
    let mut count = 0;

    let width: i32 = grid[0].len().try_into().unwrap();
    let height: i32 = grid.len().try_into().unwrap();

    for y in 1..height-1 {
        for x in 1..width-1 {
            if grid[y as usize][x as usize] != 'A' {
                continue;
            }
            let letters = format!("{}{}{}{}",
                grid[(y - 1) as usize][(x - 1) as usize], 
                grid[(y - 1) as usize][(x + 1) as usize], 
                grid[(y + 1) as usize][(x - 1) as usize],
                grid[(y + 1) as usize][(x + 1) as usize]
            );
            if letters == "SSMM" || letters == "MSMS" || letters == "MMSS" || letters == "SMSM" {
                count += 1;
            }
        }
    }

    return count;
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Unable to read file.");
    // divide by two because they get recounted the other way
    println!("Part 1: {}", part_1(input.as_str()) / 2);
    println!("Part 2: {}", part_2(input.as_str()));
    println!("Hello, world!");
}
