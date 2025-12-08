#include "../../stdc++.h"

#define ull unsigned long long

using namespace std;

vector<vector<ull>> memo;

pair<vector<vector<char>>, pair<int, int>> get_input(string filename) {
    fstream file(filename);
    string line;
    vector<vector<char>> output;
    pair<int, int> start_pos = {-1, -1};
    int row = 0;
    
    // Using getline is generally safer than >> to preserve row structure if spaces exist
    while (getline(file, line)) {
        if (line.empty()) continue;
        vector<char> row_char;
        for (int col = 0; col < line.size(); col++) {
            if (line[col] == 'S') {
                start_pos = { row, col };
            }
            row_char.push_back(line[col]);
        }
        output.push_back(row_char);
        row++; 
    }
    return { output, start_pos };
}

int part_1(pair<vector<vector<char>>, pair<int, int>> input) {
  int count = 0;
  int x = input.second.first;
  int y = input.second.second; 
  vector<vector<char>> board = input.first;
  cout << x << " " << y << endl;
  while (y < board.size()) {
    y++;
    x = 0;
    while (x < board[y].size()) {
      if (board[y - 1][x] == 'S' || board[y - 1][x] == '|') {
        bool split = false;
        if (board[y][x] == '^') {
          if (x < board.size() - 1 && board[y][x + 1] == '.') {
            board[y][x + 1] = '|';
            split = true;
          }
          if (x > 0 && board[y][x - 1] == '.') {
            board[y][x - 1] = '|';
            split = true;
          }
        } else if (board[y][x] == '.') {
          board[y][x] = '|';
        }
        if (split) count++;
        // cout << count << endl;
      }
      x++;
    } 
  }

  return count;
}

// Pass board by const reference to avoid copying
ull solve_part_2(const vector<vector<char>>& board, int x, int y) {
  int height = board.size();
  int width = board[0].size();

  // Base Case: If we reached the bottom row, that is 1 valid completed timeline
  if (y == height - 1) {
      return 1;
  }

  // Check Memoization: Have we calculated this path before?
  if (memo[y][x] != -1) {
      return memo[y][x];
  }

  ull total_timelines = 0;

  // Look at the cell BELOW the current beam (y + 1)
  // Note: The problem says beam moves downward.
  // If the NEXT cell is a splitter '^', we split.
  // If the NEXT cell is empty '.', we continue.
  
  char next_cell = board[y + 1][x];

  if (next_cell == '^') {
      // Splitter logic: Go Left and Right from the splitter's row
      // The splitter is at (x, y+1).
      // Left path starts at (x-1, y+1)
      if (x - 1 >= 0 && board[y + 1][x - 1] == '.') {
            total_timelines += solve_part_2(board, x - 1, y + 1);
      }
      // Right path starts at (x+1, y+1)
      // FIXED: Compare x against width, not height
      if (x + 1 < width && board[y + 1][x + 1] == '.') {
            total_timelines += solve_part_2(board, x + 1, y + 1);
      }
  } 
  else if (next_cell == '.') {
      // Empty space: Continue straight down
      total_timelines += solve_part_2(board, x, y + 1);
  }
  // Note: If next_cell is neither (e.g., blocked or another beam in P1 logic), 
  // the timeline ends/dies here, adding 0.

  // Save result to cache
  return memo[y][x] = total_timelines;
}

int main() {
  auto input_data = get_input("input.txt");
  vector<vector<char>> board = input_data.first;
  pair<int, int> start = input_data.second;

  if (start.first == -1) {
      cout << "Error: No Start 'S' found." << endl;
      return 1;
  }

  // Initialize memoization table with -1
  // Size: Height x Width
  memo.assign(board.size(), vector<ull>(board[0].size(), -1));

  cout << "Starting at: " << start.second << ", " << start.first << endl;

  // Start recursion
  // Note: We pass the board, and the current X, Y.
  ull p2 = solve_part_2(board, start.second, start.first);

  cout << "Part 2: " << p2 << endl;

  return 0;
}