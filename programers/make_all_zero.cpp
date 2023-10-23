// 모두 0으로 만들기  2023-10-23


#include <vector>

using namespace std;

bool vis[300000];
vector<vector<int> > adj_list(300000);

struct Node
{
    long long cnt;
    long long gap;
};

long long abs(long long n)
{
    return 0 < n ? n : -n;
}

Node dfs(int i, vector<int> &a)
{
    vis[i] = true;
    Node return_node = { 0, a[i] };
    
    for (int j: adj_list[i])
    {
        if (vis[j]) continue;
        
        Node temp = dfs(j, a);
        return_node.cnt += temp.cnt + abs(temp.gap);
        return_node.gap += temp.gap;
    }
    
    return return_node;
}

long long solution(vector<int> a, vector<vector<int>> edges)
{
    for (vector<int> edge: edges)
    {
        adj_list[edge[0]].push_back(edge[1]);
        adj_list[edge[1]].push_back(edge[0]);
    }
    
    Node temp = dfs(0, a);
    
    if (temp.gap != 0)
    {
        return -1;
    }
    
    return temp.cnt;
}
