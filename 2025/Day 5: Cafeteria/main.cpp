#include "../../stdc++.h"

using namespace std;

#define ull unsigned long long
// in type
#define range_t pair<ull, ull>
#define in_t pair<vector<range_t>, vector<ull>>

using namespace std;

in_t get_input(string filename) {
  in_t output;
  fstream file(filename);
  string line;
  bool next = false;
  while (file >> line) {
    istringstream l(line);
    char dash = ' ';
    ull a = 0, b = 0;
    l >> a >> dash >> b;
    if (dash == '-') {
      output.first.emplace_back(a, b);
    } else {
      output.second.push_back(a);
    }
  }
  return output;
}

in_t condense_input(in_t &input) {
  vector<range_t> &values = input.first;
  sort(values.begin(), values.end(), [](range_t& first, range_t& second) {
    return first.first < second.first;
  });

  ull start = values[0].first, end = values[0].second;
  vector<range_t> p;
  for (auto range : values) {
    if (end < range.first) {
      p.emplace_back(start, end);
      start = range.first, end = range.second;
    } else if (end >= range.first) {
      end = max(range.second, end);
    }
  } 
  p.emplace_back(start, end);

  return { p, input.second };
}

ull part_1(in_t input) {
  int count = 0;

  for (auto id : input.second) {
    for (auto range : input.first) {
      if (id >= range.first && id <= range.second) {
        count++;
        break;
      }
    }
  }

  return count;
}

ull part_2(in_t input) {
  ull count = 0;
  for (auto range : input.first) {
    count += range.second - range.first + 1;
  }
  return count;
}

int main() {
  auto input = get_input("input.txt");
  input = condense_input(input);
  ull p1 = part_1(input);
  ull p2 = part_2(input);
  cout << "Part 1: " << p1 << endl;
  cout << "Part 2: " << p2 << endl;
  return 0;
}
