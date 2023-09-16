// 합승 택시 요금.  2023-09-16


#include <vector>

using namespace std;

int d_list[201][201];
int adj_list[201][201];

int solution(int n, int s, int a, int b, vector<vector<int>> fares)
{
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            if (i == j) d_list[i][j] = 0;
            else d_list[i][j] = 20000000;
        }
    }
    
    for (vector<int> fare: fares)
    {
        d_list[fare[0]][fare[1]] = fare[2];
        d_list[fare[1]][fare[0]] = fare[2];
    }
    
    for (int k = 1; k <= n; ++k)
    {
        for (int i = 1; i <= n; ++i)
        {
            for (int j = 1; j <= n; ++j)
            {
                if (d_list[i][k] + d_list[k][j] < d_list[i][j])
                    d_list[i][j] = d_list[i][k] + d_list[k][j];
            }
        }
    }
    
    int ans = 400000000;
    int temp;
    for (int i = 1; i <= n; ++i)
    {
        temp = d_list[s][i] + d_list[i][a] + d_list[i][b];
        ans = ans < temp ? ans : temp;
    }
    
    return ans;
}
