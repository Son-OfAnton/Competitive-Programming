#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int src;
    int dest;
    int distance;
};

vector<int> bellmanFord(int start, int n, const vector<Edge>& graph) {
    vector<int> shortDistances(n, 30000);
    shortDistances[start - 1] = 0;

    for (int i = 0; i < n - 1; ++i) {
        for (const Edge& edge : graph) {
            int src = edge.src;
            int dest = edge.dest;
            int distance = edge.distance;

            int newDistance = shortDistances[src - 1] + distance;
            if (shortDistances[src - 1] != 30000 && newDistance < shortDistances[dest - 1]) {
                shortDistances[dest - 1] = newDistance;
            }
        }
    }

    return shortDistances;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<Edge> graph;

    for (int i = 0; i < m; ++i) {
        Edge edge;
        cin >> edge.src >> edge.dest >> edge.distance;
        graph.push_back(edge);
    }


    vector<int> shortDistances = bellmanFord(1, n, graph);

    for(int distance : shortDistances) {
        cout << distance << " ";
    }

    return 0;
}