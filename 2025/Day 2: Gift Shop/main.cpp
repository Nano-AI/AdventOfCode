#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>

#define ull unsigned long long

using namespace std;

vector<pair<ull, ull>> get_input(const char* filename) {
  fstream file(filename);
  string line;

  getline(file, line);
  stringstream ss(line);
  string part;

  vector<pair<ull, ull>> ranges;
  while (getline(ss, part, ',')) {
    if (part.empty()) continue;
    stringstream range_stream(part);
    ull a, b;
    char dash;
    range_stream >> a >> dash >> b;
    if (dash == '-') {
      ranges.emplace_back(a, b);
    }
  }
  return ranges;
}

bool is_valid_2(ull value) {
  string number = to_string(value);
  for (int i = 1; i <= number.size() / 2; i++) {
    if (number.size() % i != 0) continue;
    int j = 0;
    bool repeated = true;
    while (j < number.size() - i) {
      if (number.substr(j, i) != number.substr(j + i, i)) {
        repeated = false;
        break;
      } 
      j += i;
    }
    if (repeated) return false;
  }
  return true;
}

bool is_valid_1(ull value) {
  string s = to_string(value);
  if (s.size() % 2 != 0) return true;
  return s.substr(0, s.size() / 2) != s.substr(s.size() / 2, s.size() / 2);
}

ull solve(vector<pair<ull, ull>> input, bool (*validation_func)(ull)) {
  ull count = 0;
  for (auto &range : input) {
    for (ull i = range.first; i <= range.second; i++) {
      if (!validation_func(i)) {
        count += i;
      }
    }
  }
  return count;
}

int main() {
  vector<pair<ull, ull>> input = get_input("input.txt");
  ull p1 = solve(input, is_valid_1);
  ull p2 = solve(input, is_valid_2);
  cout << "Part 1: " << p1 << endl;
  cout << "Part 2: " << p2 << endl;
  return 0;
}
