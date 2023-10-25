// 보행자 천국.  2023-10-25


#include <vector>

using namespace std;

int MOD = 20170805;
int ni, nj;

int solution(int n, int m, vector<vector<int>> city_map)
{
    int dp[500][500][2] = { 0, };
    dp[0][1][1] = 1; dp[1][0][0] = 1;
    
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            if (city_map[i][j] == 1) continue;
            
            ni = i + 0; nj = j + 1;
            if (0 <= ni && ni < n && 0 <= nj && nj < m)
            {
                if (city_map[i][j] == 0)
                {
                    dp[ni][nj][1] = (dp[ni][nj][1] + dp[i][j][0] + dp[i][j][1]) % MOD;
                }
                else
                {
                    dp[ni][nj][1] = (dp[ni][nj][1] + dp[i][j][1]) % MOD;
                }
            }
            
            ni = i + 1; nj = j + 0;
            if (0 <= ni && ni < n && 0 <= nj && nj < m)
            {
                if (city_map[i][j] == 0)
                {
                    dp[ni][nj][0] = (dp[ni][nj][0] + dp[i][j][0] + dp[i][j][1]) % MOD;
                }
                else
                {
                    dp[ni][nj][0] = (dp[ni][nj][0] + dp[i][j][0]) % MOD;
                }
            }
        }
    }
    
    return (dp[n - 1][m - 1][0] + dp[n - 1][m - 1][1]) % MOD;
}
