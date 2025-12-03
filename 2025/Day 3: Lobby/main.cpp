#include "../../stdc++.h"
#define ull unsigned long long

using namespace std;

vector<string> get_input(string filename) {
  fstream file(filename);
  string line_value;
  vector<string> output;
  while (file >> line_value) {
    output.push_back(line_value); 
  }
  return output;
}

ull get_max_index(string line) {
  if (line.empty()) return -1;
  ull max = 0;
  for (ull i = 0; i < line.length(); i++) {
    if (line[i] > line[max]) max = i;
  }
  return max;
}

ull solve(vector<string> &input, int joltage_size) {
  ull output = 0;
  for (string line : input) {
    ull joltage = 0;
    ull power = 0;
    string current_line = line;

    int current_index = 0;
    for (int i = joltage_size - 1; i >= 0; i--)  {
      // substring from last index to length - (i)
      int start_index = current_index;
      int end_index = line.length() - i;
      string sub = line.substr(current_index, end_index - start_index);
      // cout << sub << endl;
      int max_index = get_max_index(sub);
      joltage *= 10;
      joltage += sub[max_index] - '0';
      current_index += max_index + 1;
    } 
    // cout << joltage << endl;
    output += joltage;
  }
  return output;
}

int main() {
  vector<string> input = get_input("input.txt");
  ull p1 = solve(input, 2);
  ull p2 = solve(input, 12);
  cout << "Part 1: " << p1 << endl;
  cout << "Part 2: " << p2 << endl;
  return 0;
}
