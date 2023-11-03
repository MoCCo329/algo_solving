// GPS.  2023-11-03


#include <vector>
#define INF 987654321

using namespace std;

int dp[100][201];

int solution(int n, int m, vector<vector<int>> edge_list, int k, vector<int> gps_log)
{
    for (int i = 0; i < k; ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            dp[i][j] = INF;
        }
    }
    vector<vector<int> > adj_list(n + 1);
    for (vector<int> edge: edge_list)
    {
        adj_list[edge[0]].push_back(edge[1]);
        adj_list[edge[1]].push_back(edge[0]);
    }
    
    dp[0][gps_log[0]] = 0;
    for (int i = 0; i < k - 2; ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            if (dp[i][j] == INF) continue;
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + (gps_log[i + 1] == j ? 0 : 1));
            for (int nj: adj_list[j])
            {
                dp[i + 1][nj] = min(dp[i + 1][nj], dp[i][j] + (gps_log[i + 1] == nj ? 0 : 1));
            }
        }
    }
    
    int min_cnt = INF;
    for (int i: adj_list[gps_log[k - 1]])
    {
        min_cnt = min(min_cnt, dp[k - 2][i]);
    }
    
    if (min_cnt == INF) return -1;
    return min_cnt;
}
