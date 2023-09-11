// 거리두기 확인하기.  2023-09-11


#include <string>
#include <vector>

using namespace std;

bool vis[5][5];
int d_list[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

bool dfs(int i, int j, int k, vector<string> *maps)
{
    if (k == 2) return true;
    
    for (int d = 0; d < 4; ++d)
    {
        int ni = i + d_list[d][0], nj = j + d_list[d][1];
        if (ni < 0 || 4 < ni || nj < 0 || 4 < nj || vis[ni][nj]) continue;
        if ((*maps)[ni][nj] == 'X') continue;
        if ((*maps)[ni][nj] == 'P') return false;
        vis[ni][nj] = true;
        if (!dfs(ni, nj, k + 1, maps)) return false;
        vis[ni][nj] = false;
    }
    return true;
}

bool test(vector<string> *maps)
{
    for (int i = 0; i < 5; ++i)
        for (int j = 0; j < 5; ++j)
            vis[i][j] = false;
    
    for (int i = 0; i < 5; ++i)
    {
        for (int j = 0; j < 5; ++j)
        {
            if ((*maps)[i][j] == 'P')
            {
                vis[i][j] = true;
                if (!dfs(i, j, 0, maps)) return false;
                vis[i][j] = false;
            }
        }
    }
    return true;
}

vector<int> solution(vector<vector<string>> places)
{
    vector<int> ans;
    for (vector<string> maps: places)
    {
        ans.push_back(test(&maps) ? 1 : 0);
    }
    
    return ans;
}
