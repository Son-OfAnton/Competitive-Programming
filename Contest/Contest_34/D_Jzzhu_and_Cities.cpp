#include <bits/stdc++.h>

using namespace std;

struct Edge
{
  int dest;
  int length;
  bool isTrain;
};


int main() {
    int n, m, k;
    cin >> n >> m >> k;

    const int INF = numeric_limits<int>::max();
    // make graph vector of of Edge struct length n+1
    vector<Edge> graph(n+1);


    for (int i = 0; i < m; i++) {
        int src, dest, length;
        cin >> src >> dest >> length;
        
    }

    for (int i = 0; i < k; i++) {
        int dest, length;
        cin >> dest >> length;
        // assign graph[1] to an edge with dest and length and False
        
        graph[1].push_back(make_pair(dest, length));
    }

    map<int, int> distances;
    for (int i = 1; i <= n; i++) {
        distances[i] = INF;
    }
    distances[1] = 0;

    set<int> visited;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, 1));

    while (!pq.empty()) {
        int curr_dis = pq.top().first;
        int curr_city = pq.top().second;
        pq.pop();

        if (visited.find(curr_city) != visited.end()) {
            continue;
        }
        visited.insert(curr_city);

        for (auto neighbor : graph[curr_city]) {
            int nbr = neighbor.first;
            int dis = neighbor.second;
            int new_dis = curr_dis + dis;

            if (new_dis < distances[nbr]) {
                distances[nbr] = new_dis;
                pq.push(make_pair(new_dis, nbr));
                k--;
            }
        }
    }

    cout << k << endl;

    return 0;
}
