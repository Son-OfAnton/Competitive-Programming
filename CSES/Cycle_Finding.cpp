#include <bits/stdc++.h>
#define endl "\n"
using namespace std;
#define int long long int
 
class Node
{
public:
	int src;
	int dest;
	int wgt;
};
 
int n, m;
vector<Node> edges;
vector<int> dist;
vector<int> relaxant;
 
void bellman_ford()
{
	int nodeInCycle;
	for (int i = 1; i <= n; ++i)
	{
		nodeInCycle = -1;
		for (auto e : edges)
		{
 
			int src = e.src;
			int dest = e.dest;
			int wgt = e.wgt;
			if (dist[src] + wgt < dist[dest])
			{
				dist[dest] = wgt + dist[src];
				relaxant[dest] = src;
				nodeInCycle = dest;
			}
		}
	}
 
	if (nodeInCycle == -1)
		cout << "NO" << endl;
 
	else
	{
		for (int i = 1; i <= n; ++i)
		{
			nodeInCycle = relaxant[nodeInCycle];
		}
 
		vector<int> cycle;
 
		for (int currNode = nodeInCycle;; currNode = relaxant[currNode])
		{
			cycle.push_back(currNode);
			if (currNode == nodeInCycle and cycle.size() > 1)
				break;
		}
 
		reverse(cycle.begin(), cycle.end());
 
		cout << "YES" << endl;
		for (auto node : cycle)
		{
			cout << node << " ";
		}
 
		cout << endl;
	}
}
 
int32_t main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	dist.resize(n + 1);
	relaxant.resize(n + 1);
	edges.resize(m);
 
	for (int i = 0; i < m; ++i)
	{
		struct Node inp;
		cin >> inp.src >> inp.dest >> inp.wgt;
		edges[i] = inp;
	}
 
	for (int i = 1; i <= n; ++i)
	{
		relaxant[i] = -1;
	}
	bellman_ford();
}