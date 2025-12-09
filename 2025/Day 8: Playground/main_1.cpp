#include "../../stdc++.h"

/*
i built a kd tree but honestly this too complicated for an input file that's this small
*/

using namespace std;

struct Point {
  double e[3] = { 0, 0, 0 };
  Point(double p[3]) {
    e[0] = p[0];
    e[1] = p[1];
    e[2] = p[2];
  }
  Point(double x, double y, double z) {
    e[0] = x;
    e[1] = y;
    e[2] = z;
  }
  Point() {}
  double x() {return e[0];}
  double y() {return e[1];}
  double z() {return e[2];}
  double dist_sq(Point p) {
    return pow(p.x() - x(), 2) + pow(p.y() - y(), 2) + pow(p.z() - z(), 2);
  }
  Point operator-(const Point &n) {
    return {
      e[0] - n.e[0],
      e[1] - n.e[1],
      e[2] - n.e[2]
   };
  }
  // dot product
  double dot(const Point& p) {
    return e[0] * p.e[0] + e[1] * p.e[1] + e[2] * p.e[2] ;
  }
  bool operator==(const Point& other) const {
    return e[0] == other.e[0] && e[1] == other.e[1] && e[2] == other.e[2];
  }
};

namespace std {
  template <>
  struct hash<Point> {
    size_t operator()(const Point& p) const {
      // Combine the hashes of the three coordinates
      size_t h1 = hash<double>{}(p.e[0]);
      size_t h2 = hash<double>{}(p.e[1]);
      size_t h3 = hash<double>{}(p.e[2]);
      // A common hash combination pattern to reduce collisions
      return h1 ^ (h2 << 1) ^ (h3 << 2); 
    }
  };
}

struct Node {
  Point location;
  Node* left = nullptr;
  Node* right = nullptr;
  Node* parent = nullptr;
  Node(Point location) {
    this->location = location;
  }
  Node() {}
};

class KDTree {
public:
  Node* root;
  Node* build_tree(vector<Point> &points) {
    root = build_tree(points, 0, 0, points.size());
    return root;
  }

  Point nearest_neighbor(Point &point) {
    if (!root) return Point();
    double best_dist = numeric_limits<double>::infinity();
    Node* best = nullptr;
    return nearest_neighbor(point, root, 0, best, &best_dist)->location;
  }

private:
  int k = 3;
  Node* build_tree(vector<Point> &points, int depth, int start, int end) {
    // empty points
    if (start >= end) return nullptr;
    int axis = depth % k;
    // sort if at least two elements exist
    if (start < end) {
      // sort by axis
      sort(points.begin() + start, points.begin() + end, [&](const Point& a, const Point& b) {
        return a.e[axis] < b.e[axis];
      });
    }
    // calculate median index
    int median_index = (end - start) / 2 + start;
    // store median index
    Point &median = points[median_index];
    // make a new node out of it
    Node* node = new Node(median);
    // create left subtree & right
    node->left = build_tree(points, depth + 1, start, median_index);
    node->right = build_tree(points, depth + 1, median_index + 1, end);
    // update parent values
    if (node->left != nullptr)
      node->left->parent = node;
    if (node->right != nullptr)
      node->right->parent = node;
    return node;
  }

  Node* nearest_neighbor(Point &point, Node*& current, int depth, Node*& best, double* best_dist) {
    // reached end
    if (current == nullptr) {
      return best;
    }
    // current node is closer, so update
    double l = current->location.dist_sq(point);
    if (l < *best_dist && l > 1e-9) {
      *best_dist = l;
      best = current;
    }

    int axis = depth % k;
    // |plane - point| < radius
    // (plane - point)^2 < radius^2
    // if this is true, that means that the "bad" tree COULD contain the closest node
    // as in it's in the plane past this
    double dist_to_plane = point.e[axis] - current->location.e[axis];
    double plane_dist_sq = dist_to_plane * dist_to_plane;
    // use BST
    if (current->location.e[axis] > point.e[axis]) {
      nearest_neighbor(point, current->left, depth + 1, best, best_dist);
      // check to see if we reach to the other plane
      if (plane_dist_sq < *best_dist && current->right != nullptr) {
        nearest_neighbor(point, current->right, depth + 1, best, best_dist);
      }
    } else {
      nearest_neighbor(point, current->right, depth + 1, best, best_dist);
      if (plane_dist_sq < *best_dist && current->left != nullptr) {
        nearest_neighbor(point, current->left, depth + 1, best, best_dist);
      }
    }
    return best;
  }
};

vector<Point> get_input(string filename) {
  fstream file(filename);
  Point currentPoint;
  char comma1, comma2;
  vector<Point> out;
  while (file >> currentPoint.e[0] >> comma1 >> currentPoint.e[1] >> comma2 >> currentPoint.e[2]) {
    out.push_back(currentPoint);
  }
  return out;
}

struct DSU {
  vector<int> parent;
  vector<int> size;

  DSU(int n, int connection_size) {
    parent.resize(n);
    iota(parent.begin(), parent.end(), 0);
    size.assign(n, 1);
  }

  int find(int i) {
    if (parent[i] == i) {
      return i;
    }
    parent[i] = find(parent[i]);
    return parent[i];
  }

  bool unite(int i, int j) {
    int root_i = find(i);
    int root_j = find(j);
    if (root_i != root_j) {
      if (size[root_i] < size[root_j]) swap(root_i, root_j);
      parent[root_j] = root_i;
      size[root_i] += size[root_j];
      return true;
    }
    return false;
  }

  int get_size(int i) {
    return size[find(i)];
  }
};

int main() {
  vector<Point> input = get_input("input.txt");

  unordered_map<Point, int> point_to_id;
  for (size_t i = 0; i < input.size(); i++) {
    point_to_id[input[i]] = i;
  }

  KDTree tree;
  tree.build_tree(input);

  return 0;
}
