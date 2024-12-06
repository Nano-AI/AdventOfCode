#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <map>

using namespace std;

int part_1(vector<int> a, vector<int> b) {
    int d = 0;

    for (int i = 0; i < a.size(); i++) {
        d += abs(a[i] - b[i]);
    }

    return d;
}

int part_2(vector<int> a, vector<int> b) {
    map<int, int> m;
    int o = 0;
    for (int i : b) {
        map<int, int>::iterator it = m.find(i);
        if (it == m.end()) {
            m.insert(make_pair(i, 1));
        } else {
            it->second++;
        }
    }
    for (int v : a) {
        o += v * m[v];
    }
    return o;
}

int main() {
    ifstream input("input.txt");
    // ifstream input("test.txt");
    vector<int> a, b;
    bool alt = false;
    int v;
    while (input >> v) {
        if (alt) {
            a.push_back(v);
        } else {
            b.push_back(v);
        }
        alt = !alt;
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    cout << "Part 1: " << part_1(a, b) << endl;
    cout << "Part 2: " << part_2(a, b) << endl;

    input.close();
    return 0;
}
