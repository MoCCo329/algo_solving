// 카카오프렌즈 컬러링북.  2023-11-10


#include <vector>
#include <queue>

using namespace std;

int cnt;
int max_size;
bool vis[100][100];
int d_list[4][2] = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

void init(int N, int M)
{
    cnt = 0;
    max_size = 0;
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            vis[i][j] = false;
        }
    }    
}

vector<int> solution(int N, int M, vector<vector<int> > picture)
{
    init(N, M);
    
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            if (vis[i][j] || picture[i][j] == 0) continue;
            
            cnt++;
            int temp_size = 0;
            int num = picture[i][j];
            
            queue<pair<int, int> > q;
            q.push(make_pair(i, j));
            vis[i][j] = true;
            while (!q.empty())
            {
                pair<int, int> temp = q.front();
                q.pop();
                ++temp_size;
                for (int d = 0; d < 4; ++d)
                {
                    int ni = temp.first + d_list[d][0], nj = temp.second + d_list[d][1];
                    if (ni < 0 || N <= ni || nj < 0 || M <= nj || vis[ni][nj] || picture[ni][nj] != num) continue;
                    vis[ni][nj] = true;
                    q.push(make_pair(ni, nj));
                }
            }
            max_size = max(max_size, temp_size);
        }
    }
    
    vector<int> ans(2);
    ans[0] = cnt;
    ans[1] = max_size;
    
    return ans;
}
