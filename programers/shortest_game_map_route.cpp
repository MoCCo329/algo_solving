// 게임 맵 최단거리.  2023-12-06


#include<queue>
#include<vector>

using namespace std;

int N, M;
int d_list[4][2] = { {0, 1}, {1, 0}, {-1, 0}, {0, -1} };
bool vis[100][100];

struct Pos
{
    int i;
    int j;
    int cnt;
};

int solution(vector<vector<int> > maps)
{
    N = maps.size();
    M = maps[0].size();
    
    queue<Pos> q;
    
    vis[0][0] = true;
    Pos temp = { 0, 0, 1 };
    q.push(temp);
    while (!q.empty())
    {
        Pos temp = q.front();
        q.pop();
        
        for (int d = 0; d < 4; ++d)
        {
            int di = d_list[d][0], dj = d_list[d][1];
            int ni = temp.i + di, nj = temp.j + dj;
            if (ni < 0 || N <= ni || nj < 0 || M <= nj || vis[ni][nj] || maps[ni][nj] == 0) continue;
            if (ni == N - 1 && nj == M - 1) return temp.cnt + 1;
            vis[ni][nj] = true;
            Pos pos = { ni, nj, temp.cnt + 1 };
            q.push(pos);
        }
    }
    
    return -1;
}
