#include <iostream>
#include <vector>
#include <queue>
#include <sstream>
#include <string>
#include <map>
#include <set>
#include <limits>
#include <utility>

using namespace std;

class Graph {
private:
    map<string, vector<pair<string, int>>> adjacency_list;

public:
    void add_edge(const string& u, const string& v, int weight) {
        adjacency_list[u].push_back(make_pair(v, weight));
        adjacency_list[v].push_back(make_pair(u, weight));
    }

    pair<int, vector<pair<int, string>>> dijkstra_mst(const string& source) {
        priority_queue<pair<int, string>, vector<pair<int, string>>, greater<pair<int, string>>> min_heap;
        min_heap.push(make_pair(0, source));
        int mst_cost = 0;
        vector<pair<int, string>> mst_edges;

        map<string, int> min_distance;
        for (const auto& adj : adjacency_list) {
            min_distance[adj.first] = numeric_limits<int>::max();
        }
        min_distance[source] = 0;

        set<string> visited;

        while (!min_heap.empty()) {
            auto elem = min_heap.top();
            min_heap.pop();
            string current_vertex = elem.second;

            if (visited.find(current_vertex) != visited.end()) {
                continue;
            }

            visited.insert(current_vertex);
            mst_cost += elem.first;

            if (current_vertex != source) {
                mst_edges.push_back(make_pair(elem.first, current_vertex));
            }

            for (auto& neighbor : adjacency_list[current_vertex]) {
                string adjacent = neighbor.first;
                int weight = neighbor.second;

                if (visited.find(adjacent) == visited.end() && weight < min_distance[adjacent]) {
                    min_distance[adjacent] = weight;
                    min_heap.push(make_pair(weight, adjacent));
                }
            }
        }

        return make_pair(mst_cost, mst_edges);
    }
};

vector<tuple<string, string, int>> get_input_edges() {
    vector<tuple<string, string, int>> edges;
    string line;
    cout << "Enter an edge (format: u v weight) or enter 'done' to finish:" << endl;
    
    while (getline(cin, line)) {
        if (line == "done") break;
        string u, v;
        int weight;
        istringstream iss(line);
        if (iss >> u >> v >> weight) {
            edges.push_back(make_tuple(u, v, weight));
        } else {
            cout << "Invalid input format. Please try again." << endl;
        }
    }
    
    return edges;
}

int main() {
    Graph graph;
    auto edges = get_input_edges();
    for (auto& edge : edges) {
        graph.add_edge(get<0>(edge), get<1>(edge), get<2>(edge));
    }

    string source_vertex;
    cout << "Enter the source vertex for MST: ";
    cin >> source_vertex;

    auto result = graph.dijkstra_mst(source_vertex);
    auto mst_cost = result.first;
    auto mst_edges = result.second;

    if (mst_edges.empty()) {
        cout << "Invalid source vertex. Please enter a valid vertex." << endl;
    } else {
        cout << "Minimal Spanning Tree (MST) Cost: " << mst_cost << endl;
        cout << "Minimal Spanning Tree (MST) Edges:" << endl;
        for (auto& edge : mst_edges) {
            cout << edge.second << " (Cost: " << edge.first << ")" << endl;
        }
    }
    
    return 0;
}
