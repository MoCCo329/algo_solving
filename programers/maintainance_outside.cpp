// 외벽 점검.  2023-09-17


#include <vector>
#include <algorithm>

using namespace std;

bool vis[15];
int ans = -1;
int N;

void dfs(int k, int p, int p_end, vector<int> &weak, vector<int> &dist)
{
    if (k == weak.size())
    {
        ans = p;
        return;
    }
    if (p == p_end || ans != -1) return;
    
    for (int i = 0; i < weak.size(); ++i)
    {
        if (vis[i]) continue;
        
        vector<int> temp_vis;
        int start = weak[i];
        int end = weak[i] + dist[p];
        
        vis[i] = true;
        temp_vis.push_back(i);

        for (int j = 0; j < weak.size(); ++j)
        {
            if (vis[j]) continue;
            if ((start <= weak[j] && weak[j] <= end) || (start <= weak[j] + N && weak[j] + N <= end))
            {
                vis[j] = true;
                temp_vis.push_back(j);
            }
        }
        
        dfs(k + temp_vis.size(), p + 1, p_end, weak, dist);
        
        for (int w: temp_vis)
        {
            vis[w] = false;
        }
    }
}

int solution(int n, vector<int> weak, vector<int> dist)
{
    N = n;
    sort(dist.begin(), dist.end(), greater<>());
    if (N <= dist[0]) return 1;
        
    for (int i = 1; i <= dist.size(); ++i)
    {
        dfs(0, 0, i, weak, dist);
        if (ans != -1) return ans;
    }
    
    return ans;
}
