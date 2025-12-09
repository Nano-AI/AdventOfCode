#include "../../stdc++.h"
#define ull unsigned long long 
using namespace std;

struct Point {
  double x, y, z;
  double dist_sq(const Point& other) const {
    return pow(other.x - x, 2) + pow(other.y - y, 2) + pow(other.z - z, 2);
  }
};

struct Edge {
  int u_idx, v_idx;
  double dist_sq;
  bool operator<(const Edge& other) const {
    return dist_sq < other.dist_sq;
  }
};

struct DSU {
  vector<int> parent, size;
  DSU(int n) {
    size.resize(n, 1);
    parent.resize(n);
    for (int i = 0; i < n; i++) {
      parent[i] = i;
    }
  }

  int find(int i) {
    int root = parent[i];
    if (parent[root] != root) {
      return parent[i] = find(root);
    }
    return root;
  }

  bool unite_1(int i, int j) {
    int ir = find(i);
    int jr = find(j);
    if (ir == jr) return false;

    // Union by Size logic:
    // Always attach the smaller tree to the larger tree
    if (size[ir] < size[jr]) {
        swap(ir, jr);
    }

    parent[jr] = ir;
    size[ir] += size[jr];
    return true; 
  }

  bool unite_2(int i, int j) {
    int ir = find(i);
    int jr = find(j);
    if (ir == jr) return false;
    if (size[ir] >= 2 || size[jr] >= 2) return false;
    if (size[ir] < size[jr]) {
      swap(ir, jr);
    }
    parent[jr] = ir;
    size[ir] += size[jr];
    return true;
  }

  bool all() {
    for (int i = 0; i < parent.size() - 1; i++) {
      if (parent[i] != parent[i + 1]) return false;
    }
    return true;
  }
  

  int get_size(int i) {
    return size[find(i)];
  }
};

vector<Point> get_input(string filename) {
  fstream file(filename);
  Point p;
  char comma;
  vector<Point> out;
  while (file >> p.x >> comma >> p.y >> comma >> p.z) {
    out.push_back(p);
  }
  return out;
}

ull part_1(vector<Point> points) {
  vector<Edge> edges;
  edges.reserve(points.size() * points.size() / 2);
  for (size_t i = 0; i < points.size(); ++i) {
    for (size_t j = i + 1; j < points.size(); j++) {
      edges.push_back({
        (int) i,
        (int) j,
        points[i].dist_sq(points[j])
      });
    }
  }

  sort(edges.begin(), edges.end());
  int limit = 1000;
  if (edges.size() < limit) limit = edges.size();

  DSU dsu(points.size());
  for (int i = 0; i < limit; i++) {
    dsu.unite_1(edges[i].u_idx, edges[i].v_idx);
  }

  vector<int> circuit_sizes;
  vector<bool> visited_roots(points.size(), false);

  for (size_t i = 0; i < points.size(); ++i) {
    int root = dsu.find(i);
    if (!visited_roots[root]) {
      circuit_sizes.push_back(dsu.size[root]);
      visited_roots[root] = true;
    }
  }

  sort(circuit_sizes.rbegin(), circuit_sizes.rend());

  return ((ull) circuit_sizes[0]) * ((ull) circuit_sizes[1]) * ((ull) circuit_sizes[2]);
}

ull part_2(vector<Point> points) {
  vector<Edge> edges;
  edges.reserve(points.size() * points.size() / 2);
  for (size_t i = 0; i < points.size(); ++i) {
    for (size_t j = i + 1; j < points.size(); j++) {
      edges.push_back({
        (int) i,
        (int) j,
        points[i].dist_sq(points[j])
      });
    }
  }
  sort(edges.begin(), edges.end());
  DSU dsu(points.size());
  Edge last_edge;
  for (int i = 0; i < edges.size(); i++) {
    dsu.unite_1(edges[i].u_idx, edges[i].v_idx);
    int s1 = dsu.get_size(edges[i].u_idx);
    int s2 = dsu.get_size(edges[i].v_idx);
    if (s1 == s2 && s1 == points.size()) {
      last_edge = edges[i];
      break;
    }
  }
  return ((ull) points[last_edge.u_idx].x) * ((ull) points[last_edge.v_idx].x);
}

int main() {
  vector<Point> input = get_input("input.txt");
  ull p1 = part_1(input);
  ull p2 = part_2(input);
  cout << "Part 1: " << p1 << endl;
  cout << "Part 2: " << p2 << endl;
  return 0;
}
