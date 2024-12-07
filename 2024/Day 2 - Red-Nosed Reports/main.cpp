#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int get_direction(int from, int to) {
    return (from < to) ? 1 : -1;
}

bool safe_check(string line) {
    stringstream ls(line);
    int current;
    int prev;

    int direction = 0;

    ls >> prev;

    bool safe = true;

    while (ls >> current) {
        if (direction == 0) {
            direction = get_direction(prev, current);
        }
        if (direction != get_direction(prev, current)) {
            safe = false;
            break;
        }
        int d = abs(current - prev);
        if (d < 1 || d > 3) {
            safe = false;
            break;
        }
        prev = current;
    }
    return safe;
}

int part_1(string fileName) {
    ifstream input(fileName);
    string line;
    int safe_count = 0;

    while (getline(input, line)) {
        if (safe_check(line)) safe_count++; 
    }

    input.close();

    return safe_count;
}

int part_2(string fileName) {
    // i had a solution where i used dx to calculate the step between each thing, and find the odd one out
    // but 10 cases failed on it
    ifstream input(fileName);
    string line;
    int safe_count = 0;

    while (getline(input, line)) {
        stringstream ls(line);

        bool safe = false;
        if (safe_check(line)) {
            safe_count++;
            continue;
        }
        for (int ignore = 0; ignore < line.size(); ignore ++) {
            string input = "";
            if (ignore > 0) {
                input = line.substr(0, ignore - 1);
            }
            input = input + line.substr(ignore + 1, line.size() - ignore - 1);
            safe = safe_check(input);
            // cout << input << endl;
            if (safe) {
                safe = true;
                safe_count++;
                break;
            }
        }
    }

    input.close();

    return safe_count;
}

int main() {
    string file = "input.txt";
    // cout << part_1(file) << endl;
    cout << part_2(file) << endl;
    return 0;
}
