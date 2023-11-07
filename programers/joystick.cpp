// 조이스틱.  2023-11-07


#include <string>

using namespace std;

int N;
int ans;
bool vis[20];
int d_list[2] = { 1, -1 };

void dfs(int i, int k, int cnt, string &name, int turn, int d)
{
    if (ans <= cnt || 1 < turn) return;
    if (k == N)
    {
        ans = min(ans, cnt);
        return;
    }
    
    for (int nd: d_list)
    {
        int ni = (i + nd + N) % N;
        if (!vis[ni])
        {
            vis[ni] = true;
            dfs(ni, k + 1, cnt + min(name[ni] - 'A', -(name[ni] - 'Z') + 1) + 1, name, turn + (d == nd ? 0 : 1), nd);
            vis[ni] = false;
        }
        else
        {
            dfs(ni, k, cnt + 1, name, turn + (d == nd ? 0 : 1), nd);
        }
    }
}

int solution(string name)
{
    N = name.size();
    ans = 540;
    int k = 0;
    for (int i = 1; i < N; ++i)
    {
        if (name[i] == 'A')
        {
            ++k;
            vis[i] = true;
        }
    }
    
    vis[0] = true;
    dfs(0, k + 1, min(name[0] - 'A', -(name[0] - 'Z') + 1), name, 0, 1);
    dfs(0, k + 1, min(name[0] - 'A', -(name[0] - 'Z') + 1), name, 0, -1);
    
    return ans;
}
