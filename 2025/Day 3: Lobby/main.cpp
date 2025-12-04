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

int get_max_index(string line, int start, int end) {
  int max = start;
  for (ull i = start; i < end; i++) {
    if (line[i] > line[max]) max = i;
  }
  return max;
}

ull solve(vector<string> &input, int joltage_size) {
  ull output = 0;
  for (string line : input) {
    ull joltage = 0;
    ull power = 0;
    int current_index = 0;
    for (int i = joltage_size - 1; i >= 0; i--)  {
      current_index = get_max_index(line, current_index, line.length() - i);
      joltage *= 10;
      joltage += line[current_index] - '0';
      current_index++;
    } 
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
