// 트리 트리오 중간값.  2023-10-10


#include <vector>

using namespace std;

vector<vector<int> > adj_list(250001);
bool vis[250001];
vector<int> temp_ans(3);

void find_far(int i, int d)
{
    if (temp_ans[0] < d)
    {
        temp_ans[0] = d;
        temp_ans[1] = 1;
        temp_ans[2] = i;
    } else if (temp_ans[0] == d)
    {
        temp_ans[1]++;
    }
    
    for (int j: adj_list[i])
    {
        if (vis[j]) continue;
        vis[j] = true;
        find_far(j, d + 1);
        vis[j] = false;
    }
}

int solution(int n, vector<vector<int> > edges)
{
    for (vector<int> edge: edges)
    {
        adj_list[edge[0]].push_back(edge[1]);
        adj_list[edge[1]].push_back(edge[0]);
    }
    
    int start = 1;
    vis[start] = true;
    find_far(start, 0);
    vis[start] = false;
    
    start = temp_ans[2];
    temp_ans[0] = 0, temp_ans[1] = 0, temp_ans[2] = 0;
    vis[start] = true;
    find_far(start, 0);
    vis[start] = false;
    
    if (1 < temp_ans[1]) return temp_ans[0];
    
    start = temp_ans[2];
    temp_ans[0] = 0, temp_ans[1] = 0, temp_ans[2] = 0;
    vis[start] = true;
    find_far(start, 0);
    
    if (temp_ans[1] == 1) return temp_ans[0] - 1;
    return temp_ans[0];
}
