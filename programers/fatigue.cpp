// 피로도.  2023-07-29


#include <vector>

using namespace std;

int ans = 0;
bool vis[8];

void dfs(int k, int p, vector<vector<int>>* dungeons)
{
    if (ans < k) ans = k;
    for (int i = 0; i < (*dungeons).size(); ++i)
    {
        if (vis[i] || p < (*dungeons)[i][0]) continue;
        vis[i] = true;
        dfs(k + 1, p - (*dungeons)[i][1], dungeons);
        vis[i] = false;
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    dfs(0, k, &dungeons);

    return ans;
}