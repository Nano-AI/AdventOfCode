#include "../../stdc++.h"
using namespace std;

vector<string> get_input(string filename) {
  fstream file(filename);
  string line;
  vector<string> output;
  while (file >> line) {
    output.push_back(line);
  }
  return output;
}

int part_1(vector<string> &input, bool update) {
  int height = input.size();
  int width = input[0].size();
  int count = 0;
  
  vector<string> temp = input;

  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      if (temp[i][j] != '@') continue;
      int printers = 0;
      for (int di = -1; di <= 1; di++) {
        // bound check
        if (i + di < 0 || i + di >= height) continue;
        for (int dj = -1; dj <= 1; dj++) {
          // don't count current spot
          if (di == 0 && dj == 0) continue;
          // bound check
          if (j + dj < 0 || j + dj >= width) continue;
          if (temp[i + di][j + dj] == '@') printers++; 
        }
      }
      if (printers < 4) {
        count++;
        if (update)
          input[i][j] = '.';
      }
    }
  }

  return count;
}

int part_2(vector<string> &input) {
  int s = 0;
  int rolls = 0;
  do {
    rolls = part_1(input, true);
    s += rolls;
  } while (rolls > 0);
  return s;
}

int main() {
  vector<string> input = get_input("input.txt");
  int p1 = part_1(input, false);
  int p2 = part_2(input);
  cout << "Part 1: " << p1 << endl;
  cout << "Part 2: " << p2 << endl;
}
