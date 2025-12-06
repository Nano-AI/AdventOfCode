#include "../../stdc++.h"
#define ull unsigned long long
using namespace std;

pair<vector<vector<ull>>, vector<char>> get_input_1(string filename) {
  ifstream file(filename);
  string line;

  vector<vector<ull>> out;
  vector<char> ops;

  while (getline(file, line)) {
    // Skip blank lines
    if (line.find_first_not_of(" \t") == string::npos) continue;

    // Check if this line is only operators (* or +)
    bool is_op_line = true;
    for (char c : line) {
      if (c != '*' && c != '+' && !isspace(c)) {
        is_op_line = false;
        break;
      }
    }

    if (is_op_line) {
      for (char c : line) {
        if (c == '*' || c == '+')
          ops.push_back(c);
      }
      continue;
    }

    vector<ull> nums;
    stringstream ss(line);
    ull number;
    while (ss >> number) {
        nums.push_back(number);
    }
    out.push_back(nums);
  }

  return {out, ops};
}

ull part_1(pair<vector<vector<ull>>, vector<char>> input) {
  int height = input.first.size();
  int width = input.first[0].size();
  ull out = 0;
  for (int i = 0; i < width; i++) {
    char op = (char) input.second[i];
    ull solution = (op == '*') ? 1 : 0;
    for (int j = 0; j < height; j++) {
      if (op == '+') {
        solution += input.first[j][i];
      } else if (op == '*') {
        solution *= input.first[j][i];
      }
    }
    out += solution;
  }
  return out;
}

vector<string> get_input_2(string filename) {
  fstream file(filename);
  vector<string> out;
  string line;
  while (getline(file, line)) {
    out.push_back(line);
  }
  return out;
}

ull part_2(vector<string> input) {
  ull output = 0;
  int height = input.size();
  int y = 0;
  int x = input[y].size() - 1;
  vector<ull> numbers;
  ull number = 0;
  while (true) {
    char c = input[y][x];
    if (y >= height - 1) {
      numbers.push_back(number);
      number = 0;
      if (c == '*' || c == '+') {
        ull solution = (c == '*') ? 1 : 0;
        for (auto d : numbers) {
          solution = (c == '*') ? (solution * d) : (solution + d);
        }
        output += solution;
        if (x == 0 && y == height - 1) {
          break;
        }
        x--;
        numbers.clear();
      } 
      y = -1;
      x--;
    }

    if (isdigit(c)) {
      number *= 10;
      number += c - '0';
    }
    
    y++;
  }

  return output;
}

int main() {
  pair<vector<vector<ull>>, vector<char>> input = get_input_1("input.txt");
  ull p1 = part_1(input);
  cout << "Part 1: " << p1 << endl;
  vector<string> input_2 = get_input_2("input.txt");
  ull p2 = part_2(input_2);
  cout << "Part 2: " << p2 << endl;
  return 0;
}
