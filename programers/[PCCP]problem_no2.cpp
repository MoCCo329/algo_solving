// [PCCP 기출문제] 2번.  2023-11-24


#include <vector>

using namespace std;

bool vis[500][500];
bool avail[500][1250000];
int oil_cnt;
int N, M;
int oil_size[1250000];
int d_list[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

int search(int i, int j, vector<vector<int>> &land)
{
    int cnt = 1;
    vis[i][j] = true;
    avail[j][oil_cnt] = true;
    
    for (int d = 0; d < 4; ++d)
    {
        int di = d_list[d][0], dj = d_list[d][1];
        int ni = i + di, nj = j + dj;
        if (ni < 0 || N <= ni || nj < 0 || M <= nj || vis[ni][nj] || land[ni][nj] == 0) continue;
        vis[ni][nj] = true;
        cnt += search(ni, nj, land);
    }
    
    return cnt;
}

int solution(vector<vector<int> > land)
{
    N = land.size();
    M = land[0].size();
    
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            if (vis[i][j] || land[i][j] == 0) continue;
            
            oil_size[oil_cnt] = search(i, j, land);
            ++oil_cnt;
        }
    }
    
    int max_cnt = 0;
    for (int j = 0; j < M; ++j)
    {
        int cnt = 0;
        for (int oil = 0; oil < oil_cnt; ++oil)
        {
            if (avail[j][oil])
            {
                cnt += oil_size[oil];
            }
        }
        if (max_cnt < cnt)
        {
            max_cnt = cnt;
        }
    }
    
    return max_cnt;
}
